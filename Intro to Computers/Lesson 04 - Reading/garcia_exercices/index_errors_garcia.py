# Exercise 5: IndexError - List Access Errors

# Error 1
fruits = ["apple", "banana", "cherry"]
print(fruits[2])

# 1. IndexError: list index out of range
# 2. Probably the third index
# 3. 0:2

# Error 2
# shopping_list = []
# first_item = shopping_list[0]
# print(first_item)

# 1. IndexError: list index out of range
# 2. BEcause the lsit is empty

shopping_list = []
if len(shopping_list) > 0:
    first_item = shopping_list[0]
    print(first_item)
else:
    print("Shopping list is empty")