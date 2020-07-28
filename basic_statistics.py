from random import randint

digits, x = [], 0

while x < 10:
    digits.append(randint(0, 100))
    x = x+1

print(digits)

y = min(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)


