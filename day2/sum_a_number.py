"""
    Add two digits of a two-digit number and print the result
"""
import sys

number: str = input("Enter a two-digit number: ")

try:
    if len(number) != 2:
        raise ValueError("Invalid input value!")
except ValueError:
    print("Invalid input entered!")
    sys.exit(1)

try:
    number_test = int(number) + 1
except ValueError:
    print("Not a number!")
    sys.exit(1)

print(F"The result is: {int(number[0]) + int(number[1])}")
