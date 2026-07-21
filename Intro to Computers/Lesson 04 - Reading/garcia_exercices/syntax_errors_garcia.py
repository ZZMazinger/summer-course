# Exercise 2; SyntaxError - Missing Punctuation

def calculate_total(price, quantity):
    total = price * quantity
    print(f"Total: {total}")
    return total

calculate_total(10, 5)

# Questions to answers
# 1. 5
# 2. SyntaxError: f-string: expecting '}'
# 3. Closing curly bracket and right parenthesis


# Exercise 3: NameError - Undefined Variables
def greet(name):
    print(f"Hello, {name}")

greet("Bob")

# 1. 17
# 2. SyntaxError: expected ':'
# 3. colon