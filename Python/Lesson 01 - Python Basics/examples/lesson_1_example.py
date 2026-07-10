# Lesson 1 Example

#name = input("What is your name? ")

#favnum = float(input("What is your favorite number? "))

#print("Hello,", name)
#print('Your favorite number is', favnum)
#print('Your favore number minus 10 is', favnum -10)

# Write a script that prompts the user for a diameter of the pizza and outputs the area

pizza_diameter = float(input("What is the diameter of the pizza in inches? "))
pizza_area = 3.14 * (pizza_diameter/2)**2

print(f"The pizza area is {pizza_area}.")


#Calculate the price per area
print()

pizza_price = float(input("What is the price of the pizza in $USD? "))

print(f"The price per square inch is: ${(pizza_price / pizza_area):.02f}")

# Write a script that calculates the best deal

print()

print("Now let's compare two pizzas of one size to one pizza of another size to determine the best deal.")
first_pizza_diameter = float(input('Please enter the diameter in inches of the smaller pizza size, which you would buy two of: '))
first_pizza_price = float(input('Please enter the total price for two pizzas of that size (not per pizza, but together): '))
first_pizza_area = 3.14 * (first_pizza_diameter/2)**2
first_pizza_cost = first_pizza_price / (2 * first_pizza_area)

second_pizza_diameter = float(input('Please enter the diameter in inches of the larger pizza size, which you would buy one of: '))
second_pizza_price = float(input('Please enter the price for one pizza of that size: '))
second_pizza_area = 3.14 * (second_pizza_diameter/2)**2
second_pizza_cost = second_pizza_price / second_pizza_area

print()
print(f"The first pizza deal, for two smaller pizzas, has you paying ${first_pizza_cost:.03f} per square inch.")
print(f"The second pizza deal, for one larger pizza, has you paying ${second_pizza_cost:.03f} per square inch.")
print()

if first_pizza_cost < second_pizza_cost:
    print('For the best deal, you should buy two smaller pizzas.')
elif second_pizza_cost < first_pizza_cost:
    print('For the best deal, you should buy one larger pizza.')
elif first_pizza_cost == second_pizza_cost:
    print('Both are equal. For the best deal, you should buy one larger pizza, unless you really like crust.')
else:
    print("Unexpected outcome, and I didn't do error handling. Sorry")