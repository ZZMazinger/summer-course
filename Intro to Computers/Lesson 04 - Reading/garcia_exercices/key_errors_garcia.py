# Exercise 6: KeyError - Dictionary Access Errors

# Error 1
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grade": "A"
}
print(student["grade"])

# 1. "grade" key

# Safer approach
grade = student.get("grade", "No grade available")
print(grade)

# Error 2
inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
}
print(f"We have {inventory.get('apples')} apples")

# 1. No difference from Python's perspective
# 2. Use `.get()` when you're not sure if a key exists; use `[key]` when you expect it to always exist.