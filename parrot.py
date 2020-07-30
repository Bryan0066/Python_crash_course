
message_1 = input("Tell me something, and I will repeat it back to you: ")
print(message_1)

prompt = "\n Tell me something and I will repeat it back to you:"

prompt += "\n Enter 'quit' to end the program."
'''
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)
'''
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
