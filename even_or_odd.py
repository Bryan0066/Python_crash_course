

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

if number % 10 == 0:
    print(f"\n{number} is divisible by 10.")
else:
    print(f"\n{number} is not divisible by 10.")