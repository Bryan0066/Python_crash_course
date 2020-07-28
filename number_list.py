
# 1-20 list
list_4_3 = [values*1 for values in range(1, 21)]
print(list_4_3)

"""
# 1 - 1 mil
list_4_4 = [values*1 for values in range(1, 1000001)]
for x in list_4_4:
    print(x)
# math with 1-1mil list
print("sum:",sum(list_4_4), "\nmin:", min(list_4_4),"\nmax:", max(list_4_4))
"""

# odd numbers 1-20
list_4_6 = [values*1 for values in range(1, 21, 2)]
print(list_4_6)

# x of 3, 3-30
list_4_7 = [values*1 for values in range(3, 31, 3)]
print(list_4_7)

# x of 3, 3-30
list_4_8 = [values**3 for values in range(1, 11)]
print(list_4_7)
