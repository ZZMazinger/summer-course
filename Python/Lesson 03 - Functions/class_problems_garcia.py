# Problems in class

# # Problem 1
# print()

# for number in range (1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# print()

# # Problem 2
# import random

# print()

# user_play = input('Please choose rock, paper, or scissors: ')
# comp_play = random.choice(['rock', 'paper','scissors'])

# print()
# print(f"You chose {user_play}.")
# print(f"The computer chose {comp_play}.")
# print()

# if user_play == comp_play:
#     print('You tied')
# elif user_play == 'rock' and comp_play == 'paper':
#     print('You lost')
# elif user_play == 'rock' and comp_play == 'scissors':
#     print('You won')
# elif user_play == 'paper' and comp_play == 'rock':
#     print('You won')
# elif user_play == 'paper' and comp_play == 'scissors':
#     print('You lost')
# elif user_play == 'scissors' and comp_play == 'rock':
#     print('You lost')
# elif user_play == 'scissors' and comp_play == 'paper':
#     print('You won')

# print()

# # Problem 3
# print()

# import random

# number_list = list(range(1,101))

# # random_number = random.choice(number_list)
# random_number = random.randint(1,100)

# user_guess = int(input('Please guess a number from 1 to 100: '))
# count = 1

# while user_guess != random_number:
#     if user_guess > random_number:
#         print("You guessed too high")
#     else:
#         print("You guessed too low")
#     user_guess = int(input('Please guess a number from 1 to 100: '))
#     count += 1 

# if user_guess == random_number:
#     print(f"You guessed it corectly, and it took you {count} tries.")

# print()

# # Problem 4
# print()
# num_students = int(input('How many students are in the class? '))
# student_list = []
# print()

# for number in range(num_students):
#     student_list.append(input("Please enter a student name: "))

# print()

# dict_students = {student: float(input(f"What is {student}'s numeric grade? ")) for student in student_list}

# print()

# grade_sum = 0.0
# for grade in dict_students.values():
#     grade_sum += grade
# grade_average = grade_sum/len(dict_students)
# print(f"Class Average: {grade_average}")

# print(f"Highest Grade: {max(dict_students.values())}")
# print(f"Lowest Grade: {min(dict_students.values())}")

# print()

# max_gradeholders = [stud_key for stud_key, grade_val in dict_students.items() if grade_val == max(dict_students.values())]
# print(f"Highest Grade Achiever(s): {max_gradeholders}")

# print()


# # Random Problems
# import random

# print()

# random_integer = random.randint(0, 100)

# if random_integer < 50:
#     print("The number is less than 50.")
# elif random_integer == 50:
#     print('The number is 50.')
# else:
#     print('The number is greater than 50.')

# print()
# print(f"The number is {random_integer}.")
# print()


# # Rectangle Area
# def rect_area(len: int, wid: int) -> int:
#      return len * wid

# length = int(input('Please enter an integer length: '))
# width = int(input('Please enter an integer width: '))

# print(rect_area(length, width))

# def rect_area():
#     length = int(input('Please enter an integer length: '))
#     width = int(input('Please enter an integer width: '))
#     return length * width

# print(rect_area())


# # In Class Exerise #2
# print()

# def tip(total: float, percentage: float) -> float:
#     return total * (percentage/100)

# print(tip(10, 25))
# print(f"The amount to tip is ${tip(10, 25):.2f}")


# # In Class Exercise #4
# print()

# def has_more_characters(string1: str, string2: str) -> str:
#     if len(string1) > len(string2):
#         return string1
#     elif len(string1) < len(string2):
#         return string2
#     else:
#         return 'Both strings are equal in length.'
    
# str1 = input('Please enter a string: ')
# print()
# str2 = input('Please enter another string: ')
# print()

# print(f"The string with more characters is: {has_more_characters(str1, str2)}")

# print()


# # In Class Exercise #5
# print()

# def count_char_x(word, character):
#     counter = 0
#     for chara in word:
#         if chara == character:
#             counter += 1
#     return counter

# longstring = input('Please enter a word: ')
# char = input('Please enter a character: ')

# character_count = count_char_x(longstring, char)

# print(f"There is/are {character_count} instance(s) of the character {char} in the word {longstring}.")

# print()


##### Lesson 01-03 Optional Review #####

# # Problem 1 - Temperature Advisor
# print()

# current_temp = float(input('Enter the current temperature: '))

# print()

# if current_temp < 40:
#     print('Wear a coat')
# elif current_temp <=65:
#     print('Bring a jacket')
# else:
#     print('Enjoy the weather!')

# print()

# is_raining = input('Is it raining? (yes/no) ')

# print()

# if is_raining == 'yes':
#     print('Bring an umbrella')
# elif is_raining == 'no':
#     pass
# else:
#     print('You should have entered only "yes" or "no"')

# print()

# # Problem 1 - Temperature Advisor (Better Solution)
# print()

# current_temp = float(input('Enter the current temperature: '))
# is_raining = input('Is it raining? (yes/no) ')

# if current_temp < 40:
#     output = 'Wear a coat.'
# elif current_temp <=65:
#     output = 'Bring a jacket.'
# else:
#     output = 'Enjoy the weather!'

# print()

# if is_raining == 'yes':
#     output += ' Bring an umbrella.'

# print(output)
# print()


# # Problem 2 - FizzBuzz with a Twist
# print()

# def fizz_buzzer(start: int, end: int) -> None:
#     stop = end + 1
#     count = 0
#     for number in range(start, stop):           # Note that I could have done end+1 right here, even without extra parenthesis
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#             count += 1
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
#     else:
#         print('\nTotal number of FizzBuzz lines:', count)
#     # Note that I could have returned count here and then changed the later print call accordingly

# fizz_buzzer(int(input('Enter an integer Start Value: ')), int(input('Enter an integer End Value: ')))

# print()


# # Problem 3 - Password Checker
# print()

# number_tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# # Note that it would be better to do if letter == letter.upper():
# upper_tuple = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

# def has_number(your_string):
#     for char in your_string:
#         if char in number_tuple:
#             return True

# def has_upper(your_string):
#     for char in your_string:
#         if char in upper_tuple:
#             return True

# def check_password(password):
#     if len(password) < 8:
#         return 'Weak'
#     elif len(password) >= 8 and has_number(password) == True and has_upper(password) == True:
#         return 'Strong'
#     else:
#         return 'Medium'

# user_password = input('Please enter your password: ')
# check_password(user_password)

# while check_password(user_password) != 'Strong':
#     print('Please enter a stronger password, with at least one uppercase letter and at least one number.')
#     print()
#     user_password = input('Please enter your password: ')
#     print()
# else:
#     print('Strong password.')
#     print()


# Problem 4 - Grade Calculator

def letter_grade(score):
    if float(score) < 60:
        score = 'F'
        return score
    elif float(score) < 70:
        score = 'D'
        return score
    elif float(score) < 80:
        score = 'C'
        return score
    elif float(score) < 90:
        score = 'B'
        return score
    else:
        score = 'A'
        return score

number_of_scores = int(input('How many test scores do you want to enter? '))
cumulative_score = 0
class_average = 0
min_placeholder = 100
max_placeholder = 0

for student in range(number_of_scores):
    student_grade = float(input('Enter student grade (numeric): '))
    print(student_grade, letter_grade(student_grade))
    cumulative_score += student_grade
    if student_grade < min_placeholder:
        min_placeholder = student_grade
    elif student_grade > max_placeholder:
        max_placeholder = student_grade

class_average = cumulative_score / number_of_scores

print(f"Class average is {class_average:.1f}%, which denotes a letter grade of {letter_grade(class_average)}")
print(f"Maximum score in class: {max_placeholder}")
print(f"Minimum score in class: {min_placeholder}")
print()