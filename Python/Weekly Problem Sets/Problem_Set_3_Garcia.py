# Student Code for Problem Set 3 - Importing Modules - Miguel Garcia

# # Problem 1 - Dice Roll Simulator
# # Input: number of dice, sides
# # Output: dice rolls

# import random

# # Function which returns one die roll of given sides
# def roll(sides: int) -> int:
#     return random.randint(1, sides)

# # Function which rolls multiple dice
# def roll_many(num_dice: int, sides: int) -> list:
#     roll_results = []
#     for die in range(num_dice):
#         each_roll = roll(sides)
#         roll_results.append(each_roll)
#     return roll_results

# # Random Seed
# # random.seed(42)
# # This is useful to establish consistency and reproduceability of results.

# # Scenario
# twoD6 = roll_many(2, 6)
# oneD20 = roll(20)
# threeD8 = roll_many(3, 8)

# # 1000 Loops
# total_damage = 0
# for iteration in range(1000):
#     iter_damage = sum(roll_many(3, 8))
#     total_damage += iter_damage

# # Print the results
# print(f"""
# === MOVEMENT CHECK (2d6) ===
# Roll 1: {twoD6[0]}  Roll 2: {twoD6[1]}  Total: {sum(twoD6)}

# === ATTACK CHECK (1d20) ===
# Roll: {oneD20}{" - CRITICAL HIT!" if oneD20 == 20 else ""}

# === DAMAGE ROLL (3d8) ===
# Rolls: {threeD8}  Total: {sum(threeD8)}  Average: {round(sum(threeD8)/len(threeD8), 1)}

# === SIMULATION (1000 damage rolls) ===
# Simulated average total: {round((total_damage/1000), 2)}
# Theoretical average:     13.5
# """)

# # Battle Quotes
# quote_list = ['Sun Tzu (The Art of War): "If you know the enemy and know yourself, you need not fear the result of a hundred battles."',
#               'Winston Churchill: "Never in the field of human conflict was so much owed by so many to so few."',
#               'Ulysses S. Grant: "In every battle there comes a time when both sides consider themselves beaten, then he who continues the attack wins."',
#               'Julius Caesar: "Veni, vidi, vici" (I came, I saw, I conquered).',
#               'George S. Patton: "Nobody ever defended anything successfully, there is only attack and attack and attack some more."',
#               'Lord Horatio Nelson: "England expects that every man will do his duty."']
# print(random.choice(quote_list))
# print()


# # Problem 2 - Space Mission Calculator
# # Input: x1, y1, x2, y2, radius, mass, velocity
# # Output: NAVIGATION REPORT - Distance to station, Orbit circumference, Kinetic energy (fuel), Log10 of velocity

# import math

# # Define a function to calculate the straight-line distance between two points in space using the distance formula
# def distance(x1: float, y1: float, x2: float, y2: float) -> float:
#     dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
#     return dist

# # Define a function that calculates the circumference of a circular orbit
# def orbit_circumference(radius: float) -> float:
#     circum = 2 * math.pi * radius
#     return circum

# # Define a function that calculates kinetic energy, then returns the result rounded to 2 decimal places using math.floor()
# def fuel_needed(mass: float, velocity: float) -> float:
#     kinetic_energy = .5 * mass * velocity**2
#     return math.floor(100*kinetic_energy)/100

# # Define a bearing function for the challenge section
# def bearing(x1: float, y1: float, x2: float, y2: float) -> float:
#     rads = math.atan2(y2 - y1, x2 - x1)
#     degs = math.degrees(rads)
#     return degs

# # Mission Data
# ship_pos = (0, 0)
# station_pos = (143, 892)
# orbit_radius = 6371       # km (Earth's radius)
# ship_mass = 50000         # kg
# ship_velocity = 7800      # m/s
# log10 = math.log(ship_velocity, 10)
# # Taking the base-10 logarithm of a spaceship's velocity represents the order of magnitude of its speed.
# # It condenses massive ranges of velocity into a single, easy-to-read scale, where each whole-number increase represents a 10-fold jump in speed.

# # Do calculations
# dist = distance(ship_pos[0], ship_pos[1], station_pos[0], station_pos[1])
# circum = orbit_circumference(orbit_radius)
# kinetic_energy = fuel_needed(ship_mass, ship_velocity)

# # Print output
# print(f"""
# === NAVIGATION REPORT ===
# Distance to station:    {round(dist, 2)} units
# Orbit circumference:    {round(circum, 2)} km
# Kinetic energy (fuel):  {kinetic_energy} J
# Log10 of velocity:      {round(log10, 2)}
# """)

# # Challenge: Bearing and Ceil/Floor - Ceiling rounds up to the next integer, whereas floor roudns down to the previous integer
# angle = bearing(ship_pos[0], ship_pos[1], station_pos[0], station_pos[1])
# print(f"""Bearing to station:   {round(angle, 2)}°
# Distance ceiling:   {math.ceil(dist)}
# Distance floor:     {math.floor(dist)}
# """)


# # Problem 3 - Animal Habitat Drawing
# # input: turtle commands
# # output: yellow sun, grass strip, blue pond, three trees

# # Import and set things up and start in the upper right
# import turtle
# import random
# turtle.setup(width=800, height=600)
# turtle.screensize(800, 600)
# t = turtle.Turtle()
# t.speed(0)
# t.penup()

# # Will need the tree_x position later and default height
# tree_x = -200
# height = 50

# # Yellow sun function
# def draw_sun(t: float, x: float, y: float) -> None:
#     t.goto(x, y)
#     t.pendown()
#     t.color('yellow')
#     t.begin_fill()
#     t.circle(50)
#     t.end_fill()
#     t.penup()

# # Trees function
# def draw_tree(t: float, x: float, y: float, height: float) -> None:
#     global tree_x
#     t.goto(x, y)
#     t.color('brown')
#     t.pensize(5)
#     t.pendown()
#     t.setheading(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(10)
#     t.color('green')
#     t.pensize(1)
#     t.begin_fill()
#     t.circle(25)
#     t.end_fill()
#     t.color('brown')
#     t.pensize(5)
#     t.setheading(0)
#     t.forward(10)
#     t.right(90)
#     t.forward(height)
#     t.penup()
#     t.left(90)
#     tree_x += height # This line is only for offsetting the first three trees and doesn't do anything with random placement(s)

# # Draw Sun
# draw_sun(t, 300, 225)

# # Grass strip
# t.color('green')
# t.goto(-250, -200)
# t.pendown()
# t.begin_fill()
# t.goto(-250, -100)
# t.setheading(0)
# t.forward(600)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(600)
# t.end_fill()
# t.penup()

# # Blue Pond
# t.goto(-200, -150)
# t.color('blue')
# t.pendown()
# t.begin_fill()
# t.circle(20)
# t.end_fill()
# t.penup()

# # Draw Trees
# for tree in range(3):
#     draw_tree(t, tree_x, -100, height)

# # Challenge: 10 more random trees (mine may overlap); range for placing trees: -250 is the furthest left x, all on -100 y
# for x_start in range(10):
#     tree_x = random.randint(-250, 250)
#     height = random.randint(40, 100)
#     draw_tree(t, tree_x, -100, height)

# # View the artwork
# t.hideturtle()
# turtle.exitonclick()


# # Problem 4 - Animal Guessing Game
# # Input: User guesses number
# # Output: secret animal revealed

# # Import random and math
# import random
# import math

# # Randomly generate a secret number, with a seed for testing purposes
# random.seed(0)
# random_number = random.randint(1,100)

# # Initialize a wrong guess to start the loop, a count, animal list, and guess list
# user_guess = 0
# count = 0
# abs_dist = 0
# animals = ["Dog", "Cat", "Elephant", "Tiger", "Lion", "Giraffe", "Narwhal", "Monkey", "Zebra", "Nautilus", "Kangaroo"]
# animal_dict = {i: animals[i % len(animals)] for i in range(1, 101)}
# guess_list = []

# # Print header
# print()
# print('=== ANIMAL GUESSING GAME ===')
# print('A secret animal is waiting...')
# print()

# # # Solicit initial guess
# # user_guess = int(input('Guess a number (1-100): '))
# # guess_list.append(user_guess)
# # abs_dist = math.fabs((user_guess - random_number))
# # if abs_dist < 10:
# #     hint = 'HOT!'
# # elif abs_dist < 20:
# #     hint = 'WARM'
# # elif abs_dist < 40:
# #     hint = 'COLD'
# # else:
# #     hint = 'ICE COLD'
# # print(f"Hint: {hint}\n")
# # count += 1 

# # Guesing game
# while user_guess != random_number:
#     user_guess = int(input('Guess a number (1-100): '))
#     guess_list.append(user_guess)
#     abs_dist = math.fabs((user_guess - random_number))
#     if abs_dist <= 10:
#         hint = 'HOT!'
#     elif abs_dist <= 20:
#         hint = 'WARM'
#     elif abs_dist <= 40:
#         hint = 'COLD'
#     else:
#         hint = 'ICE COLD'
#     print(f"Hint: {hint}\n")
#     count += 1 

# if user_guess == random_number:
#     print(f"""CORRECT! The secret animal was: {animal_dict[user_guess]}
# You guessed it in {count} tries.
# Minimum possible guesses (optimal): {math.ceil(math.log2(100))} # Binary search strategy is optimal
# Mean Guess: {math.fsum(guess_list)/len(guess_list)}
# """)


# Problem 5 - Square Spiral
# Input: How many times around the square and color mode
# Output: Turtle draws a spiral

# Import turtle
import turtle

# Get user input on how many times to go around
times_around = int(input("\nHow many times around the square? "))

# Challenge section:
color_mode = input("\nSelect a color mode (rainbow/red/orange/yellow/blue/green/purple): ")

# Initialize turtle with screen and fast speed
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

# Start with side length of 10
length = 10
total_sides = times_around * 4

# Color options for rainbow mode
rainbow_colors = ["red", "orange", "yellow", "blue", "green", "purple"]

# Set color mode and draw; modulo wraps an incremending index back to zero (rainbow mode)
for i in range(total_sides):
    if color_mode == "rainbow":
        t.color(rainbow_colors[i % len(rainbow_colors)])
    else:
        t.color(color_mode)

    t.forward(length)
    t.right(90)
    length += 5

# Finish strong
t.hideturtle()
turtle.done()