from random import randint

friend = {
    'first_name': 'kevin',
    'last_name': 'smith',
    'age': '96',
    'city': 'boston',
    'fav_words': ["hey", "yo", 'bro'],
}

friend_1 = {
    'first_name': 'barb',
    'last_name': 'smithh',
    'age': '9',
    'city': 'seattle',
    'fav_words': ['yay', 'ay', 'k'],
}

friend_2 = {
    'first_name': 'bill',
    'last_name': 'smi',
    'age': '6',
    'city': 'new york',
    'fav_words': ["ah", "br", 'yu'],
}

friends = [friend, friend_1, friend_2]

first_name = friend['first_name']
first_name = first_name.title()

last_name = friend['last_name']
last_name = last_name.title()

print(f"\n\nMy friends name is {first_name} {last_name}, he is {friend['age']} years old\n"
      f"and he lives in {friend['city']}\n")

for dic in friends:
    for key, item in dic.items():
        if key == "first_name":
            print(f"First name: {item.title()}")
        if key == "last_name":
            print(f"Last name: {item.title()}")
        if key == "age":
            print(f"Age: {item.title()}")
        if key == "fav_words":
            x = randint(0, len(item)-1)
            print(f"fav_word: {item[x]}\n")