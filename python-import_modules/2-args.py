#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1  # exclude the script name

    if argc == 0:
        print("0 arguments.")
    else:
        if argc == 1:
            print("1 argument:")
        else:
            print(f"{argc} arguments:")

        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")
