#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    val = 0

    for i in range(len(sys.argv) - 1):
        val += int(sys.argv[i + 1])

    print(f"{val}")
