
motorcycles = ['yamaha', 'honda', "suzuki"]


motorcycles[0] = 'ducati'

motorcycles.append("ducati")

motorcycles_1 = []

motorcycles_1.append("yamaha")
motorcycles_1.append("honda")

motorcycles.insert(0, 'look at me, im the 0 now')

print(motorcycles)

motorcycles.remove('honda')

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(f"The first motorcycle I owned was a {popped_motorcycle}.")

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(f"\nA{too_expensive.title()}is too expensive for me")