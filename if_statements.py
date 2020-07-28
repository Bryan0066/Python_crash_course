
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")



# saying if (list), asks if theres anything in the list
if banned_users:
    for banned_user in banned_users:
        print(f'{banned_user}, you really do be banned')
    print('\n you be done')
else:
    print("you aint banned")
