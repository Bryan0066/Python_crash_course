

from random import randint

print("Welcome to the guessing game!")

number = randint(0, 100)
print(number)
guess = "WRONG"

while guess == "WRONG":
    response = int(input())
    try:
        value = int(response)
    except ValueError:
        print("This value es invalido senior, please try agaien.")
        continue
    value = int(response)
    if value < number:
        print("too low guy")
    elif value > number:
        print("too high snoop")
    else:
        print("ya did it")
        guess = "correct"
print('ya done now')



