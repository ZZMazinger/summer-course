# Lesson 6 Notes

# Pre-Class Problem 1
import random

with open('rand_ints.txt', 'w') as file:
    for line in range(100):
        random_number = random.randint(1,1000)
        file.write(str(random_number) + "\n")

with open('rand_ints.txt', 'r') as input_file:
    lines = input_file.readlines()
    lines_stripped = [line.strip() for line in lines] # List Comprehension
    count = 0
    min = 1000
    max = 0
    sum = 0
    for line in lines_stripped:
        amount = int(line)
        sum += amount
        count += 1
        if amount > max:
            max = amount
        elif amount < min:
            min = amount
    average = sum/count

    print(f"Max: {max}, Min: {min}, Average: {average}")