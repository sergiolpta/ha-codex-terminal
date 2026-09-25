#!/usr/bin/python3
"""Normalize harmless Bubblewrap preflight diagnostics for Codex."""

from __future__ import annotations

import os
import signal
import subprocess
import sys

REAL_BWRAP = "/opt/codex-sandbox/bwrap.real"
PROC_ERRORS = (
    b"Invalid argument",
    b"Operation not permitted",
    b"Permission denied",
)


def normalize_proc_error(stderr: bytes) -> bytes:
    lines = stderr.splitlines(keepends=True)
    for index, line in enumerate(lines):
        for error in PROC_ERRORS:
            old = b"bwrap: Can't mount proc on /proc: " + error
            if line.rstrip(b"\r\n") == old:
                lines[index] = line.replace(b"on /proc:", b"on /newroot/proc:", 1)
                break
    return b"".join(lines)


def main() -> int:
    with subprocess.Popen(
        [REAL_BWRAP, "--cap-drop", "ALL", *sys.argv[1:]],
        stderr=subprocess.PIPE,
        close_fds=False,
    ) as child:
        previous_handlers = {}

        def forward_signal(signum: int, _frame: object) -> None:
            child.send_signal(signum)

        for signum in (signal.SIGHUP, signal.SIGINT, signal.SIGQUIT, signal.SIGTERM):
            previous_handlers[signum] = signal.signal(signum, forward_signal)
        try:
            _, stderr = child.communicate()
        finally:
            for signum, handler in previous_handlers.items():
                signal.signal(signum, handler)

    returncode = child.returncode
    sys.stderr.buffer.write(normalize_proc_error(stderr) if returncode > 0 else stderr)
    sys.stderr.buffer.flush()
    if returncode < 0:
        signum = -returncode
        if signum not in (signal.SIGKILL, signal.SIGSTOP):
            signal.signal(signum, signal.SIG_DFL)
        os.kill(os.getpid(), signum)
        return 128 + signum
    return returncode


if __name__ == "__main__":
    sys.exit(main())
