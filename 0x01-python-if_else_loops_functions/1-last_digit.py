#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = ((number * -1) % 10) * -1

else:
    last_digit = number % 10

if last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")

elif last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d}")
    print("and is greater than 5")

else:
    print(f"Last digit of {number:d} is {last_digit:d}")
    print("and is less than 6 and not 0")