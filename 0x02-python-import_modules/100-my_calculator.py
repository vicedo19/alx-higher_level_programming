#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    count = len(argv)

    if count != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    operator = argv[2]

    def not_found():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == "+":
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
        exit()

    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
        exit()

    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
        exit()

    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
        exit()

    else:
        print(not_found())
