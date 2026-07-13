### Hands-On #1: Python Conditional Statements ###

# # Exercise 1: Check if a Number is Positive
# print()
# number1 = int(input('Provide an integer number: '))
# print()
# if number1 > 0:
#     print('The number is positive.')
# print()

# # Exercise 2: Even or Odd
# print()
# number2 = int(input('Provide an integer number: '))
# print()
# if number2 % 2 == 0:
#     print('The number is even.')
# else:
#     print('The number is odd.')
# print()

# # Exercise 3: Age Category
# print()
# age = int(input('Please enter your age as an integer: '))
# print()
# if age < 13:
#     print('You are a child.')
# elif age <= 19:
#     print('You are a teenager.')
# elif age <= 64:
#     print('You are an adult.')
# else:
#     print('You are a senior citizen.')
# print()

# # Exercise 4: Compare Two Numbers
# print()
# first_number = float(input('Please provide the first of two numbers: '))
# second_number = float(input('Please provide the second of two numbers: '))
# print()
# if first_number > second_number:
#     print('First number is larger.')
# elif first_number < second_number:
#     print('Second number is larger.')
# else:
#     print('The numbers are equal.')
# print()

# # Exercise 5: Grade Converter
# print()
# grade = float(input('Please enter your numeric grade: '))
# if grade >= 90:
#     print('A')
# elif grade >= 80:
#     print('B')
# elif grade >= 70:
#     print('C')
# elif grade >= 60:
#     print('D')
# else:
#     print('F')
# print()

# # Exercise 6: String Length Check
# print()
# user_string = input("Please enter a string: ")
# if len(user_string) > 10:
#     print('Long string')
# else:
#     print('Short string')
# print()

# # Exercise 7: Logical AND Operator
# print()
# user_number = float(input('Please enter a number: '))
# if user_number >= 10 and user_number <= 20:
#     print('Number is in range')
# else:
#     print('Out of range')
# print()

# # Exercise 8: Logical OR Operator
# print()
# maybe_vowel = input('Please enter a single letter: ')
# if maybe_vowel == 'a' or maybe_vowel == 'e' or maybe_vowel == 'i' or maybe_vowel == 'o' or maybe_vowel == 'u' or maybe_vowel == 'y':
#     print('Vowel')
# else:
#     print('Consonant, or maybe you entered a number or special character if you ignored the instructions')
# print()

# # Exercise 9: Leap Year Checker
# print()
# year = int(input('Please enter a year: '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('Leap year')
# else:
#     print('Not a leap year')
# print()

# # Exercise 10: Nested Conditionals - BMI Calculator
# print()
# user_weight = float(input('Please enter your weight in kilograms: '))
# user_height = float(input('Please enter your height in meters: '))
# user_bmi = user_weight / user_height**2

# if user_bmi < 18.5:
#     print('Underweight')
# elif user_bmi < 25:
#     print('Normal weight')
# elif user_bmi < 30:
#     print('Overweight')
# else:
#     print('Obese')
# print()

### Hands-On #2 ###

# # Exercise 11: Create and Print a List
# print()
# colors = ['cyan', 'dark gray', 'blue']

# for color in colors:
#     print(color)
# print()

# # Exercise 12: List Length
# print()
# number_list = [1, 2, 3, 4, 5]
# print(f"The list has {len(number_list)} items.")
# print()

# # Exercise 13: Append to a List
# print()
# my_list = []
# my_list.append(1)
# my_list.append(2)
# my_list.append('three')
# my_list.append('fore')
# my_list.append('fife')
# print(my_list)
# print()

# # Exercise 14: Loop Through a Range
# print()
# for number in range(1,11):
#     print(number)
# print()

# # Exercise 15: Sum Numbers in a List
# print()
# numbers = [4, 7, 2, 9, 12]
# sum = 0
# for number in numbers:
#     sum += number
# print(sum)

# # Exercise 16: List Membership
# available_fruits = ["apple", "banana", "orange", "mango"]
# fruit = "banana"

# if fruit in available_fruits:
#     print('In stock')
# else:
#     print('Out of stock')
# print()

# # Exercise 17: Count Even Numbers
# print()
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_sum = 0
# for number in numbers:
#     if number % 2 == 0:
#         even_sum += 1
# print(f"There are {even_sum} even numbers.")
# print()

# # Exercise 18: While Loop Countdown
# print()
# count = 10
# while count > 1:
#     print(count)
#     count -= 1
# print(count)
# print()

# # Exercise 19: While Loop with Condition
# print()
# number = 1
# while number <= 100:
#     print(number)
#     number *= 2
# print()

# # Exercise 20: Create a List with Range
# print()
# even_list = []
# for num in range(0, 21):
#     if num % 2 == 0:
#         even_list.append(num)
# print(even_list)
# print()