# Notes for Lesson 2

# # Exercise - Conditional Statements
# print()
# number = float(input('Please enter a number: '))

# if number == 0:
#     print('Your number is zero.')
# elif number > 0:
#     print('Your number is positive.')
# else:
#     print('Your number is negative.')

# print()

# # Instructor Led Examples (Loops)
# print()

# user_num = int(input('Please enter an even integer number: '))

# while user_num % 2 !=0:
#     user_num = int(input('Please enter an even integer number: '))

# print()
# print('Good job! You entered an even number.')
# print()

# Second Example (Loops)
print()
secret_number = 22
user_guess = int(input('Guess an integer number between 1 and 100: '))
guess_counter = 1

while user_guess != secret_number:
    if guess_counter > 5:
        break

    if user_guess < secret_number:
        print('Your guess was too low.')
    else:
        print('Your guess was too high.')
    user_guess = int(input('Guess an integer number between 1 and 100: '))
    guess_counter += 1

if user_guess == secret_number:
    print(f"Congratulations on guessing the number, {user_guess}")
    print(f"It took you {guess_counter} guesses.")
else:
    print('You did not succeed.')