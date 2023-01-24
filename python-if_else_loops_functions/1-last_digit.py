#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = (number * -1) % 10
    digit = -1 * digit
else:
    digit = number % 10
if digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
elif digit < 6 and digit != 0:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
elif digit > 5:
    print(f"Last digit of {number} is {number %10} and is greater than 5")
