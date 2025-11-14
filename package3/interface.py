# package3/interface.py

from package1 import core
from package2 import scientific

def run_calculator():
    print("Welcome to the CI/CD Calculator!")
    print("Available operations: add, sub, mul, div, pow, sqrt, exit")

    while True:
        op = input("\nOperation: ").strip().lower()
        if op == "exit":
            print("Goodbye.")
            break

        if op == "sqrt":
            a = float(input("Enter number: "))
            print("Result:", scientific.square_root(a))
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if op == "add":
                print("Result:", core.add(a, b))
            elif op == "sub":
                print("Result:", core.subtract(a, b))
            elif op == "mul":
                print("Result:", core.multiply(a, b))
            elif op == "div":
                print("Result:", core.divide(a, b))
            elif op == "pow":
                print("Result:", scientific.power(a, b))
            else:
                print("Unknown operation.")

