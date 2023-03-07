#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
new_num = number

if (number < 0):
    new_num *= -1

last_digit = new_num % 10

print(f"Last digit of {number:d} is {last_digit:d} and is", end=" ")
if (last_digit > 5):
    print("greater than 5")
elif (last_digit < 6 and last_digit != 0):
    print("less than 6 and not 0")
else:
    print("0")
