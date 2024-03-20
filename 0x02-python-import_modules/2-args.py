#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Subtract 1 to exclude the script name from the count
    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))
    for idx in range(arg_count):
        print("{}: {}".format(idx + 1, sys.argv[idx + 1]))
