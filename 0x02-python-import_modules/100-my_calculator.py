#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/":div}

    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    val1 = int(sys.argv[1])
    val2 = int(sys.argv[3])
    print("{} {} {} = {}".format(val1, sys.argv[2], val2, ops[sys.argv[2]](val1, val2)))
