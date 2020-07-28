# 3-8

import random

places = input("Where would you like to go? Separated by commas\n")

print(places)

places_list = places.split(",")

print("list:", places_list)


even_numbers = list(range(2, 11, 2))

print(even_numbers)


squares = []

for value in range(1, 11):
    squares.append(value**2)
print(squares)


x = 0

while x < 10:


