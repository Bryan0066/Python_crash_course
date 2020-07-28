
users = ['dave', 'lauren', 'kevin', 'jill', 'admin']

if users:
    for person in users:
        if person == 'admin':
            print(f"Hello {person.title()}, would you like to see a status report?")
        else:
            print(f"Hello {person.title()}, welcome!")
else:
    print("who be there")