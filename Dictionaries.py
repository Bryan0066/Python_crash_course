
alien_o = {'color': 'green', 'points': 5}
#print(alien_o['color'])

alien_o['x_position'] = 0
alien_o["y_position"] = 25
alien_o["speed"] = "medium"
#print(alien_o)

#(f"Original position: {alien_o['x_position']},{alien_o['y_position']}")

if alien_o['speed'] == "slow":
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_o['x_position'] = alien_o['x_position'] + x_increment

#print(f"New position: {alien_o['x_position']}")

del alien_o['points']
#print(alien_o)

point_value = alien_o.get("points", 'No point value assigned')

#print(point_value)

alien_1 = {'color': "yellow", 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = []

for alien in aliens:
    x = 1
    #print(alien)

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'


for alien in aliens[:5]:
    print(alien)
    print('...')

print(f"total number of aliens:{len(aliens)}")



