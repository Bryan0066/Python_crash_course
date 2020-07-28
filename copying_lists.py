

my_foods = ['pizza', 'burger', 'fries', 'ice cream', "i'm hungry"]

friend_foods = my_foods[:]

print(friend_foods)

print(my_foods[0:2])
print(my_foods[-2:])
print(my_foods[2:4])

my_foods.append("banana")
friend_foods.append("apple")

print('my favorite pizzas are:')
for pizza in my_foods:
    print(pizza, '\n')

print('-----\n')

print('my amigos favorite pizzas are:', '\n')
for pizza in friend_foods:
    print(pizza, '\n')