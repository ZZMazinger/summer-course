# Exercise 9: Reading Stack Traces

def divide_numbers(a, b):
    result = a / b
    return result

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    count = len(numbers)
    avg = divide_numbers(total, count)
    return avg

def process_scores(score_list):
    average = calculate_average(score_list)
    print(f"Average score: {average}")
    return average

# This will cause an error
scores = []
process_scores(scores)

# process_scores calls divide_numbers first
# process_scores does calculate_average last
# actual error in line 4, because line 9 has a length of zero assigned to count
# ZeroDivisionError

# Line 20 calls process_scores(); line 14 calls calculate_average(); line 10 calls divide_numbers(); line 4 causes the error