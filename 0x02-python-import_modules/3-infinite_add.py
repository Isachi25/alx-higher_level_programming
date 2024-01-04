#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    sum = 0
    for i in range(arg_count):
        sum += int(sys.argv[i + 1])
        print(sum)
