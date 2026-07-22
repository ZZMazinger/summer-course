# # Pre Class Problem 1 - The ULTIMATE RPS Simulation (20 min)
# import random

# def rps():
#     global game_count
#     global win_count
#     global loss_count

#     user_play = input('Please choose rock, paper, or scissors: ')
#     comp_play = random.choice(['rock', 'paper','scissors'])

#     print()
#     print(f"You chose {user_play}.")
#     print(f"The computer chose {comp_play}.")
#     print()

#     if user_play == comp_play:
#         print('You tied this game\n')
#     elif user_play == 'rock' and comp_play == 'paper':
#         print('You lost this game\n')
#         loss_count += 1
#     elif user_play == 'rock' and comp_play == 'scissors':
#         print('You won this game\n')
#         win_count += 1
#     elif user_play == 'paper' and comp_play == 'rock':
#         print('You won this game\n')
#         win_count += 1
#     elif user_play == 'paper' and comp_play == 'scissors':
#         print('You lost this game\n')
#         loss_count += 1
#     elif user_play == 'scissors' and comp_play == 'rock':
#         print('You lost this game\n')
#         loss_count += 1
#     elif user_play == 'scissors' and comp_play == 'paper':
#         print('You won this game\n')
#         win_count += 1

#     game_count += 1

# # print()

# number_of_games = int(input('How many games of rock-paper-scissors would you like to play? Enter an odd integer from 1-9: '))
# game_count = 0
# win_count = 0
# loss_count = 0

# while number_of_games < 1 or number_of_games > 9:
#     number_of_games = int(input('Number of games must be between 1 and 9: '))

# while number_of_games % 2 == 0:
#     number_of_games = int(input('Number of games must be odd: '))


# for game in range(number_of_games):
#     rps()
#     print(f"Wins: {win_count}, Losses: {loss_count}")
#     if win_count > number_of_games/2:
#         print('\nYou win the match already!\n')
#         print('\n"ASCI Art" =D <==3\n')
#         break
#     elif loss_count > number_of_games/2:
#         print('\nYou lost the match already!\n')
#         print('\n"ASCI Art" =(] <==3\n')
#         break


# # Pre Class Problem 3 - A simple function

# def comp_int(principal: float, interest_rate: float, time_years: int, times_per_year: int = 1) -> float:
#     amount = principal * (1 + (interest_rate/times_per_year))**(times_per_year*time_years)
#     return amount

# principal = float(input('Please enter your principal amount in $: '))
# interest_rate = float(input('Please enter the interest rate as a fraction (not %)'))
# times_per_year = int(input('Please enter the number of times interest is compounded per year: '))
# time_years = int(input('Please enter the time in years: '))

# print(f"Amount: ${comp_int(principal, interest_rate, time_years, times_per_year):.2f}") # Actually not the best way to truncate to two decimal places


# # Manipulating Files Practical

# # 100 random integers ranging from 50 to 100 into a file
# import random

# integer_list = []

# for number in range(100):
#     selected_number = random.randint(50, 100)
#     integer_list.append(str(selected_number))

# with open('integer_list.txt', 'w') as file:
#     file.write("\n".join(integer_list))


# # Read the file, find the minimum, maximum, and average values without min() or max() functions
# with open('integer_list.txt', 'r') as file:
#     min_placeholder = 100
#     max_placeholder = 50
#     sum_placeholder = 0

#     for line in file:
#         int_line = int(line)
#         sum_placeholder += int_line
#         if int_line < min_placeholder:
#             min_placeholder = int_line
#         elif int_line > max_placeholder:
#             max_placeholder = int_line

#     print(f"""
#           Minimum: {min_placeholder}
#           Maximum: {max_placeholder}
#           Average: {sum_placeholder/100}
#           """)


# # Preferred solution
# with open('file.txt', 'w') as file:
#     for line in range(100):
#         random_number = random.randint(50,100)
#         file.write(str(random_number) + "\n")

# with open('file.txt', 'r') as input_file:
#     lines = input_file.readlines()
#     lines_stripped = [line.strip() for line in lines]
#     count = 0
#     min = 1000
#     max = 0
#     sum = 0
#     for line in lines_stripped:
#         amount = int(line)
#         sum += amount
#         count += 1
#         if amount > max:
#             max = amount
#         elif amount < min:
#             min = amount
#     average = sum/count

#     print(f"Max: {max}, Min: {min}, Average: {average}")



# Hands-On Exercises: Python os and os.path Modules


# Hands-On #1
# import os
# from pathlib import Path

# Exercise 0: Environment setup
# Did git clone https://github.com/shafe123/AI2C-python-files.git in the terminal

# # Exercise 1: Get Current Working Directory
# print(os.getcwd())

# # Exercise 2: Change Directory
# os.chdir('projects')

# # Exercise 3: List Directory Contents
# print(os.listdir())

# # Exercise 4: Create a Directory
# os.mkdir('data')

# # Exercise 5: Create Nested Directories
# os.makedirs('a/b/c')

# Exercise 6: Remove a File
# os.remove('../AI2C-python-files/temp.txt')
# for file in Path('../AI2C-python-files').iterdir():
#     print(file)

# # Exercise 7: Remove an Empty Directory

# # First delete the files, which I had to look up online
# for item in Path('../AI2C-python-files/old_data').iterdir():
#     if item.is_file():
#         item.unlink(missing_ok=True)

# # Then delete the directory
# os.rmdir('../AI2C-python-files/old_data')

# # Exercise 8: Rename a File
# os.rename('../AI2C-python-files/example.txt', '../AI2C-python-files/renamed_example.txt')

# # Exercise 9: Check File or Directory Type
# print(f"Is a directory? {Path('../AI2C-python-files/target').is_dir()}")
# print(f"Is a file? {Path('../AI2C-python-files/target').is_file()}")


# Hands-On #2
import os
from pathlib import Path

# Exercise 10: Create and Write to a File
p = Path('projects') / 'log.txt'
p.write_text('single line')

# Exercise 11: Read the File
print(p.read_text())

# Exercise 12: Append a Line to the File
with open('projects/log.txt', 'a') as file:
    file.write('\nsecond line')

print(p.read_text())

# Exercise 13: Write Multiple Lines
writing_list = ['line 1', 'line 2', 'line 3']

with open('projects/multi.txt', 'w') as file:
    file.writelines(line + "\n" for line in writing_list)

# Exercise 14: Read a File Line by Line
with open('projects/multi.txt', 'r') as file:
    line_list = file.readlines()
    for line in line_list:
        print(line, end="")

# Exercise 15: Count Lines in a File
print(f"Number of lines: {len(line_list)}") # I solved this in an easier but maybe not preferred way

# Exercise 16: Read a File Safely
try:
    with open('missing_file.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')

# Exercise 17: Use pathlib to Read/Write
p = Path('projects') / 'read-write.txt'
p.write_text('Sample Text')
print(p.read_text())

# Stretch Goals
from datetime import datetime, timezone

p = Path('AI2C-python-files') / 'data.csv'
print(f"{p.stat().st_size} bytes")
last_modified_date = datetime.fromtimestamp((p.stat().st_mtime), tz=timezone.utc)
print(f"Last modified: {str(last_modified_date)[:19]}") # This can't be the best way to truncate date/time, but it works