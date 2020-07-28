

# using :3 or similar, we can grab any part of the list. remember negative numbers
players = ['charles', 'billy', 'kevin', 'bevin', 'kharles']
print(players[:3])

print('here are the first three players on the team:')
for name in players[:3]:
    print(name.title())