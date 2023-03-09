#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

n = abs(number) % 10
if number < 0:
    n *= -1

print(f"Last digit of {number} is {n} and is ", end="")

if n > 5:
    print(f"greater than 5")
elif n < 6 and n != 0:
    print(f"less than 6 and not 0")
elif n == 0:
    print(f"0")
