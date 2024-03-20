#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # Start the total sum at 0
    total_sum = 0
    # Iterate over all arguments except the first one (script name)
    for arg in sys.argv[1:]:
        # Convert each argument to an integer and add it to the total sum
        total_sum += int(arg)
    print(total_sum)
