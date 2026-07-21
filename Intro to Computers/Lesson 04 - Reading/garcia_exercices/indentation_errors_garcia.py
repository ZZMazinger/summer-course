# Exercise 8: IndentationError - Spacing Issues

# Error 1
def calculate_sum(a, b):
    result = a + b
    return result

# 1. IndentationError: expected an indented block after function definition on line 4
# 2. 4

# Error 2
def check_grade(score):
    if score >= 90:
        grade = "A"
        print(f"Grade: {grade}")  # Wrong indentation
    return grade
 
print(check_grade(95))