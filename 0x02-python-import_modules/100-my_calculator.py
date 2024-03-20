#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Check if the number of arguments is exactly 3 (script name + 3 arguments = 4 total)
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Assign command line arguments to variables
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Determine the operation based on the operator argument and execute it
    if operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        # If the operator is not recognized, print an error message and exit
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
