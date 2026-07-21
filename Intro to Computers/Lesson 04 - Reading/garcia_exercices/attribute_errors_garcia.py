# Exercise 7: AttributeError - Wrong Methods

# Error 1
text = "hello world"
print(text + "!")

# 1. text.append("!")  # append() is for lists, not strings
#    ^^^^^^^^^^^
# AttributeError: 'str' object has no attribute 'append'
# 2. .append()
# 3. text is a String

# Error 2
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# Error 3
result = print("Hello")  # print() returns None
length = result.upper()  # Can't call .upper() on None

# 1. Print always returns None implicitly because it does not return a value
# 2. dir()
# 3. A method is an action that it can perform, whereas an attribute is a characteristic