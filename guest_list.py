
dinner_guests = ["kevin", "bob", "sue", "bro"]

for x in dinner_guests:
    print(f"Hey {x}, come to my home to eat food.\n")

absent = "kevin"

dinner_guests.remove(absent)

new_guest = "billy bob"
dinner_guests.append(new_guest)
print("-----------------------")

for x in dinner_guests:
    print(f"Hey {x}, come to my home to eat food.\n")

print("-----------------------")

for x in dinner_guests:
    print(f"Hey {x}, bigger table message.\n")

newnew_guest = 'keevin'
length_of_dinner_guests =int(len(dinner_guests)/2)

dinner_guests.insert(0,new_guest)
dinner_guests.insert(length_of_dinner_guests,newnew_guest)

print(dinner_guests)