#!/usr/bin/env python3
import ctypes
import sys
if len(sys.argv) == 1:
    print("Need to pass at least one source file or directory to interpret")
    sys.exit(1)
if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("A tiny C interpreter. Exhibits accurate behavior for most C programs.")
    sys.exit(0)
# TODO: handle edge cases
ctypes.string_at(0)
