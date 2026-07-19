# Student Code for Problem Set 2 - Control Flow & Functions - Miguel Garcia

# # Problem 1 - Pizza Party Planner
# print() # Initial readibility spacing

# # Inputs for first function: people, slices_per_person, slices_per_pizza
# # Outputs for first function: how many whole pizzas to order (rounded up)

# # Inputs for second function: people, slices_per_person, slices_per_pizza
# # Outputs for second function: how many slices will be left over

# # Final Output: Print the PARTY SUMMARY
# import math

# # Define the function to calculate number of pizzas needed
# def pizzas_needed(people: int, slices_per_person: float, slices_per_pizza: int, extra_percent: int=0) -> int:
#     slices_needed = people * (100 + extra_percent)/100 * slices_per_person
#     whole_pizzas = math.ceil(slices_needed / slices_per_pizza)
#     slices_ordered = whole_pizzas * slices_per_pizza
#     return whole_pizzas, slices_ordered, slices_needed

# # Define a function to calculate number of leftover slices
# def slices_remaining(slices_ordered: int, slices_needed: float) -> int:
#     leftovers = int(slices_ordered - slices_needed)
#     return leftovers

# # Ask for how many guests, slices per person, and slices per pizza
# guests = int(input('How many people are eating pizza? '))
# slices_per_guest = float(input('How many slices per person? '))
# pizza_size = int(input('How many slices per pizza? '))


# # Call the functions and print the results

# pizzas_to_order, slices_ordered, slices_needed = pizzas_needed(guests, slices_per_guest, pizza_size, 15)
# leftover_slices = slices_remaining(slices_ordered, slices_needed)

# print(f"""
# === PIZZA PARTY PLANNER ===
# How many guests?\t{guests}
# Slices per person:\t{slices_per_guest}
# Slices per pizza:\t{pizza_size}

 
# === PARTY SUMMARY ===
# Guests:\t\t\t{guests}
# Pizzas to order:\t{pizzas_to_order}
# Total slices:\t\t{slices_ordered}
# Leftover slices:\t{leftover_slices}
# """)


# Problem 2 - Space Station Oxygen Monitor
# Input: hourly O2 readings
# Output: O2 status level

# # Define function to return oxygen criticality level
# def o2_status(level: int) -> str:
#     if level < 15:
#         return "CRITICAL"
#     elif level < 19:
#         return "LOW"
#     elif level <= 23:
#         return "NORMAL"
#     else:
#         return "HIGH"
    
# # Define a trend function to determine improving, declining, or stable
# def trend(readings):
#     if readings[-1] > readings[-2] and readings[-2] > readings[-3]:
#         return "IMPROVING"
#     elif readings[-1] < readings[-2] and readings[-2] < readings[-3]:
#         return "DECLINING"
#     else:
#         return "STABLE"

# # O2 readings (percentage) and starting counts
# readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]
# hour_count = 1
# critical_count = 0
# low_count = 0
# normal_count = 0
# high_count = 0

# # Loop to process each reading
# for reading in readings:
#     status = o2_status(reading)
#     print(f"Hour {hour_count}:{' ' * (2-len(str(hour_count)))} {reading}% - {status}")
#     if reading < 15:
#         critical_count += 1
#         print('*** ALERT: TAKE ACTION IMMEDIATELY ***')
#     elif reading < 19:
#         low_count += 1
#     elif reading <= 23:
#         normal_count += 1
#     else:
#         high_count += 1
#     hour_count += 1

# # Print status summary
# print(f"""
# === STATUS SUMMARY ===
# NORMAL:    {normal_count} hour(s)
# LOW:       {low_count} hours(s)
# CRITICAL:  {critical_count} hour(s)
# HIGH:      {high_count} hour(s)
# """)

# # Print stability trend
# print(f"Based on the last three readings, the trend is {trend(readings)}")
# print()


# # Problem 3 - RPG Character Battle
# # Input:  Starting HP values
# # Output: Battle Reults

# # Import random
# import random

# # Define the attack function
# def attack(defender_hp: int, damage: int) -> int:
#     damage = critical_hit(damage)
#     defender_hp = max((defender_hp - damage), 0)
#     return defender_hp

# # Define the life function
# def is_alive(hp: int) -> bool:
#     if hp > 0:
#         return True

# # Define the critical hit function, which I want to apply to both the hero and the monster to make it more interesting (and logical)
# def critical_hit(damage: int) -> int:
#     if random.randint(1,10) > 8:
#         damage = damage *2
#         print('*** CRITICAL HIT! ***')
#     return damage

# # Starting Values and Round Count
# hero_hp = 100
# monster_hp = 90
# round = 1
# hero_attack_damage = 18
# monster_attack_damage = 12

# # Battle Start and Loop
# print()
# print('=== BATTLE START ===')
# while is_alive(hero_hp) and is_alive(monster_hp):
#     monster_hp = attack(monster_hp, hero_attack_damage)
#     if is_alive(monster_hp):
#         hero_hp = attack(hero_hp, monster_attack_damage)
#     print(f"Round {round}:\tHero HP: {hero_hp}\t|\tMonster HP: {monster_hp}")
#     round += 1

# # Declare victory / defeat
# print()
# if not is_alive(hero_hp):
#     print('MONSTER WINS! The hero has been defeated')
# elif not is_alive(monster_hp):
#     print('HERO WINS! The monster has been defeated.')
# print()

# # Problem 4 - Mission Clearance System
# # Input: fitness score, rank, TIS
# # Output: Clearance report
# print()

# # Define Fitness Function
# def check_fitness(score: int) -> bool:
#    if score >= 70:
#        return True
#    else:
#        return False

# # Define Rank Function
# def check_rank(rank: str) -> bool:
#     if rank == 'Corporal' or rank == 'Sergeant' or rank == 'Lieutenant':
#         return True
#     else:
#         return False

# # Define TIS function
# def check_service_years(years: int) -> bool:
#     if years >= 2:
#         return True
#     else:
#         return False

# # Define a clearance checker function
# def soldier_checker(fitness: bool, rank: bool, service: bool) -> bool:
#     if fitness and rank and service:
#         return True
#     else:
#         return False

# # Ask for user inputs through a function
# def input_getter():
#     soldier_name = input("Enter your name: ")
#     fitness_score = int(input("Enter your fitness score as an integer: "))
#     soldier_rank = input("Enter your rank, spelled out with the first letter capitalized: ")
#     soldier_years = int(input("Enter your time in service as an integer: "))
#     return soldier_name, fitness_score, soldier_rank, soldier_years

# # Call the input_getter function
# soldier_name, fitness_score, soldier_rank, soldier_years = input_getter()

# # Do the three checks and store as booleans
# fitness_check = check_fitness(fitness_score)
# rank_check = check_rank(soldier_rank)
# service_check = check_service_years(soldier_years)
# clearance_check = soldier_checker(fitness_check, rank_check, service_check)

# # Store the three check functions in a list of tuples alongside their labels and input values: (partially duplicative of what comes next)
# checklist = ('Fitness check', 'Rank check', 'Service check')
# checks = [
#     (checklist[0], fitness_check, fitness_score),
#     (checklist[1], rank_check, soldier_rank),
#     (checklist[2], service_check, soldier_years)
# ]

# # Use a for loop to store results IAW instructions (I did not do this the most efficient way; sorry)
# check_results = []
# for check_name, check, value in checks:
#     result = "PASS" if check == True else "FAIL"
#     check_results.append((check_name, result, value))

# # Print the Clearance Report
# print(f"""
# SOLDIER NAME: {soldier_name}
# FITNESS SCORE: {fitness_score}
# RANK: {soldier_rank}
# YEARS OF SERVICE: {soldier_years}

# === MISSION CLEARANCE REPORT ===
# Soldier: {soldier_name}
# """)
# for check_name, result, value in check_results:
#     print(f"  {check_name}:   \t{result}")
# print()
# print('FINAL STATUS: CLEARED FOR MISSION.' if clearance_check else 'FINAL STATUS: NOT CLEARED FOR MISSION.')


# # Problem 5 - Sports Leaderboard
# # Input: list of athletes
# # Output: leaderboard

# # Define function to return goals per game roudned to 2 decimal places
# def goals_per_game(goals: int, games: int) -> float:
#     if games == 0:
#         return 0.0
#     else:
#         goals_per = round((goals / games), 2)
#         return goals_per

# # Define MVP function
# def mvp_candidate(gpg: float) -> bool:
#     if gpg >= 0.25:
#         return True
#     else:
#         return False

# # Originally provided data (athlete_name, games_played, goals_scored)
# athletes = [
#     ("Jordan",  82, 15),
#     ("Patel",   78, 22),
#     ("Okonkwo", 90, 18),
#     ("Li",      65, 9),
#     ("Reyes",   88, 31),
#     ("Fischer", 72, 14)
# ]

# # Instantiate variables for later use
# top_scorer = ''
# max_score = 0

# # Process each athlete, call functions, and print leaderboard with a for loop
# print(f"""
# === SEASON LEADERBOARD ===
# Athlete       Games   Goals   GPG     MVP?
# ------------------------------------------""")
# for athlete in athletes:
#     gpg = goals_per_game(athlete[2], athlete[1])
#     mvp = mvp_candidate(gpg)
#     mvp_marker = '*' if mvp else ''
#     if athlete[2] > max_score:
#         top_scorer = athlete[0]
#         max_score = athlete[2]
#     print(f"{athlete[0]}\t\t{athlete[1]}\t{athlete[2]}\t{gpg}\t{mvp_marker}")

# # Print Top Scorer
# print(f"\nTop scorer: {top_scorer} ({max_score} goals)")


# Problem 5 - Sports Leaderboard (Challenge Version)
# Input: list of athletes
# Output: leaderboard, including grade

# Define function to return goals per game roudned to 2 decimal places
def goals_per_game(goals: int, games: int) -> float:
    if games == 0:
        return 0.0
    else:
        goals_per = round((goals / games), 2)
        return goals_per

# Define MVP function
def mvp_candidate(gpg: float) -> bool:
    if gpg >= 0.25:
        return True
    else:
        return False

# Define grading function
def grade(gpg: float) -> str:
    if gpg < .15:
        return 'F'
    elif gpg < .18:
        return 'D'
    elif gpg < .2:
        return 'C'
    elif gpg < .25:
        return 'B'
    else:
        return 'A'

# Originally provided data (athlete_name, games_played, goals_scored)
athletes = [
    ("Jordan",  82, 15),
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14)
]

# Make a new list with room for grades
graded_athletes = []

# Instantiate variables for later use
top_scorer = ''
max_score = 0

# Process each athlete, call functions, and print leaderboard with a for loop that also adds grades to each row
print(f"""
=== SEASON LEADERBOARD ===
Athlete       Games   Goals   GPG     Grade     MVP?
------------------------------------------""")
for athlete in athletes:
    gpg = goals_per_game(athlete[2], athlete[1])
    mvp = mvp_candidate(gpg)
    mvp_marker = '*' if mvp else ''
    athlete = athlete + (grade(gpg),)
    graded_athletes.append(athlete)
    if athlete[2] > max_score:
        top_scorer = athlete[0]
        max_score = athlete[2]
    print(f"{athlete[0]}\t\t{athlete[1]}\t{athlete[2]}\t{gpg}\t{athlete[3]}\t{mvp_marker}")

# Print Top Scorer
print(f"\nTop scorer: {top_scorer} ({max_score} goals)\n")

# Print a grade distribution summary after the leaderboard using a for loop and a dictionary to count grades
distribution_summary = {'A': 0,
                        'B': 0,
                        'C': 0,
                        'D': 0,
                        'F': 0
}

# Increment the values in the dictionary for grades
for athlete in graded_athletes:
    if athlete[3] == 'A':
        distribution_summary['A'] += 1
    elif athlete[3] == 'B':
        distribution_summary['B'] += 1
    elif athlete[3] == 'C':
        distribution_summary['C'] += 1
    elif athlete[3] == 'D':
        distribution_summary['D'] += 1
    else:
        distribution_summary['F'] += 1

# Print the grade distribution summary
print('===== Grade Distribution =====')
for key, value in distribution_summary.items():
    print(f"\t{key}: {value} athlete(s)")
print()