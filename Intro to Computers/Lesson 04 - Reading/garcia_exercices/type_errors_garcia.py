# Exercise 4: TypeError - Wrong Data Types

# Error 1
age = 25
message = "I am " + str(age) + " years old"
print(message)

# 1. str and int
# 2. concatenation (+)
# 3. cast age to string or do the concatenation inside of print()


# Error 2
quantity = "5"
price = 10.50
total = int(quantity) * price
print(total)

# 1. TypeError trying to multiply string by float


# Error 3
scores = [85, 90, 78, 92]
index = 2
print(scores[index])