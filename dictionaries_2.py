
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],

}

friends = ['phil', 'sarah', ]

language = favorite_languages['sarah']

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s fav languages are:")
    for language in languages:
        print(f"\t{language.title()}")
print("\n")
for name in favorite_languages:
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love {language}")


if "erin" not in favorite_languages.keys():
    print('\n\nErin, please take our poll!')

for name in sorted(favorite_languages):
    print(f'{name.title()}, thank you for taking the poll.')



