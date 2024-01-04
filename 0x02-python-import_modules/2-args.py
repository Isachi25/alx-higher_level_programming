#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    print("{} argument{}{}"
            .format(arg_count, "" if arg_count == 1 else "s", "." if arg_count == 0 else ":"))

    i = 1
    while i <= arg_count:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
