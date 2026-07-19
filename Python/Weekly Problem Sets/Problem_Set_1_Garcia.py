# Student Code for Problem Set 1 - Python Basics -> Miguel Garcia

################################
# # Problem 1 - Introduction Card
# name = input('What is your first name? ').strip().title() #specified first name, reducing chance of length exceeding favorite number line
# favorite_number = input('What is your favorite number? ')

# favorite_number_line = '*  Your favorite number is ' + str(favorite_number) + '  *' #followed instructions literally, establishing the length of this line as the baseline
# name_greeting = '*  Hello, ' + name + '!'

# # My code assumes that the favorite number line has greater length than the name greeting line, which is a small but known gap
# # I see now that I could have used max() to determine necessary length, but I would not have done that on my own without seeing Solution 1c, so I didn't change my work

# print()
# print('Problem #1 - Introduction Card')
# print()
# print('*' * len(favorite_number_line))
# print(name_greeting, ' '*(len(favorite_number_line)-len(name_greeting)-3), '*')
# print(favorite_number_line)
# print('*' * len(favorite_number_line))
# print()

# # Type Conversions
# print('Raw input type:', type(favorite_number)) #name is also of type string, which is more obvious and not shown here
# print('As int:', int(favorite_number), ' --> ', type(int(favorite_number)))
# print('As float:', float(favorite_number), ' --> ', type(float(favorite_number)))
# print()

# # Problem 1 as a function that takes name and favorite number and favorite symbol as parameters
# name = input('What is your first name? ').strip().title() #specified first name, reducing chance of length exceeding favorite number line
# favorite_number = input('What is your favorite number? ')
# decorative_symbol = input('What is your favorite single-character symbol?' )

# def intro_card(first_name, fav_num, dec_symbol):
#     favorite_number_line = dec_symbol + '  Your favorite number is ' + str(favorite_number) + '  ' + dec_symbol #followed instructions literally, establishing the length of this line as the baseline
#     name_greeting = dec_symbol + '  Hello, ' + first_name + '!'
    
#     print()
#     print('Problem #1 - Introduction Card')
#     print()
#     print(dec_symbol * len(favorite_number_line))
#     print(name_greeting, ' ' * (len(favorite_number_line)-len(name_greeting)-3), dec_symbol)
#     print(favorite_number_line)
#     print(dec_symbol * len(favorite_number_line))
#     print()

#     # Type Conversions
#     print('Raw input type:', type(favorite_number)) #name is also of type string, which is more obvious and not shown here
#     print('As int:', int(favorite_number), ' --> ', type(int(favorite_number)))
#     print('As float:', float(favorite_number), ' --> ', type(float(favorite_number)))
#     print()

# intro_card(name, favorite_number, decorative_symbol)


# # Problem 1 with maximum length comparison; should have done 
# name = input('What is your first name? ').strip().title()
# favorite_number = input('What is your favorite number? ')
# decorative_symbol = input('What is your favorite single-character symbol?' )

# def intro_card(first_name: str, fav_num: int, dec_symbol: str) -> None:
#     favorite_number_line = dec_symbol + '  Your favorite number is ' + str(favorite_number) + '  ' + dec_symbol
#     name_greeting = dec_symbol + '  Hello, ' + first_name + '!'

#     if len(favorite_number_line) >= len(name_greeting):
#         print()
#         print('Problem #1 - Introduction Card')
#         print()
#         print(dec_symbol * len(favorite_number_line))
#         print(name_greeting, ' ' * (len(favorite_number_line)-len(name_greeting)-3), dec_symbol)
#         print(favorite_number_line)
#         print(dec_symbol * len(favorite_number_line))
#         print()
#     else:
#         print()
#         print('Problem #1 - Introduction Card')
#         print()
#         favorite_number_line = dec_symbol + '  Your favorite number is ' + str(favorite_number)
#         print(dec_symbol * (len(name_greeting)+2))
#         print(name_greeting + ' ' + dec_symbol)
#         print(favorite_number_line, ' ' * (len(name_greeting)-len(favorite_number_line)-1), dec_symbol)
#         print(dec_symbol * (len(name_greeting)+2))
#         print()

#     # Type Conversions
#     print('Raw input type:', type(favorite_number)) #name is also of type string, which is more obvious and not shown here
#     print('As int:', int(favorite_number), ' --> ', type(int(favorite_number)))
#     print('As float:', float(favorite_number), ' --> ', type(float(favorite_number)))
#     print()

# intro_card(name, favorite_number, decorative_symbol)

################################
# # Problem 2 - Sequence Explorer
# print() #spacing away from the first problem for readability
# print('Sequence Explorer')
# print()

# # Part 1
# for integer in range(1,16): #iterate over range in a for loop
#     print(integer, end=' ') #change end character from newline to a space

# print() # create line in between answer sequences

# # Part 2
# for integer in range (2, 31):
#     if integer %2 ==0: #used modulo here, though I probably could have just used step in range instead
#         print(integer, end=' ')

# print() # create line in between answer sequences

# # Part 3
# for integer in range(20, -1, -2): #use start, stop, and step
#     print(integer, end=' ')

# #ease of legibility
# print()
# print()

# # Advanced
# print('Advanced Portion')
# print()
# start_value = int(input('Please enter an integer start value: '))
# stop_value = int(input('Please enter an integer end value: ')) + 1 #Add one since the stop value is not inclusive
# step_value = int(input('Please enter an integer step value: '))

# print()
# for integer in range(start_value, stop_value, step_value): #pass user inputs
#     print(integer, end=' ') #print results

# #ease of legibility
# print()
# print()


# # Problem 2 - Sequence Explorer *** In-Class version, as a function that asks the user for inputs and does the advanced portion ***
# def sequence_explorer() -> None:
#     print()
#     start_value = int(input('Please enter an integer start value: '))
#     stop_value = int(input('Please enter an integer end value: ')) + 1 #Add one since the stop value is not inclusive
#     step_value = int(input('Please enter an integer step value: '))

#     print()
#     for integer in range(start_value, stop_value, step_value): #pass user inputs
#         print(integer, end=' ') #print results

#     print()
#     print()

# sequence_explorer()

# # Note: It would have been more Pythonic to define parameters for this function

################################
# # Problem 3 - Drill Sergeant Fitness Test
# print()
# print('Drill Sergeant Fitness Test')
# print()

# # Ask for user inputs and convert some strings to integers or floats
# soldier_name = input('ENTER SOLDIER NAME: ').strip().title()
# rank = input('ENTER RANK: ').strip().upper()
# push_ups = int(input('PUSH-UPS COMPLETED: '))
# run_time = float(input('2-MILE RUN TIME (minutes): '))

# print(f"\n=== AFTER-ACTION REPORT ===\nSoldier: {rank} {soldier_name}\nPush-ups: {push_ups}\n2-mile run: {run_time:.2f} minutes\nAverage pace: {run_time/2:.2f} minutes per mile\nDISMISSED.\n")

################################
# Problem 4 - Road Trip Fuel Calculator

# Initial planning
# Inputs: distance of trip in miles, car MPG, price of gas
# Outputs: number of gallons needed and total fuel cost

# # Define the function
# def trip_fuel(distance, efficiency, price):

#     # Calculate gallons needed
#     gallons = distance / efficiency

#     # Print outputs with labels for all output values
#     print()
#     print('--- Road Trip Fuel Estimate ---')
#     print(f"Distance:\t {distance} miles")
#     print(f"Fuel efficiency: {efficiency} MPG")
#     print(f"Gas price:\t ${price:.2f} / gallon")
#     print(f"Gallons needed:\t {gallons:.2f} gallons")
#     print(f"Total fuel cost: ${gallons * price:.2f}\n")

#     # Separate Price Scenarios with range()
#     print('--- Price Scenarios ---')
#     for cost in range(int(price*100), int(price*100 + 101), 50): #calculate in cents since range arguments must be integers
#         print(f"Gas @ ${(cost/100):.2f}/gal:  Total = ${((cost*gallons)/100):.2f}") #convert back to dollars during print
#     print()

# # Whimsical labeling
# print()
# print('Road Trip Fuel Calculator')
# print()

# # Ask for user inputs and cast to float
# trip_distance = float(input('Please enter the distance of the trip in miles: '))
# fuel_efficiency = float(input("Please enter the car's fuel efficiency in miles per gallon (MPG): "))
# gas_price = float(input('Please enter the price of gas per gallon in US dollars ($): '))

# # Call the function
# trip_fuel(trip_distance, fuel_efficiency, gas_price)