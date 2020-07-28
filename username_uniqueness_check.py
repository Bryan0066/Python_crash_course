
current_users = ['Userme', 'User', 'Coolcat55', 'beeznees88', 'itsmeboi22']

new_username = ['coolCat55', 'Username', 'beeznees88']

current_users_lower = current_users[:]

for user in range(len(current_users_lower)):
    current_users_lower[user] = current_users_lower[user].lower()

print(current_users_lower)

for i in new_username:
    if i in current_users_lower:
        print("username taken")
    else:
        print('username available')


list_1 = [values*1 for values in range(1, 10)]
print(list_1)

for number in list_1:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
