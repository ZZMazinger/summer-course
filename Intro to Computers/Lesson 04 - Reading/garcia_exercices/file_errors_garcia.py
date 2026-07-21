# Exercise 10: FileNotFoundError - Missing Files

# # Error 1
# with open("nonexistent_file.txt", "r") as file:
#     content = file.read()
#     print(content)

# 1. FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
# 2. nonexistent_file.txt
# 3. The current directory

import os

filename = "nonexistent_file.txt"

# Check if file exists first
if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)
else:
    print(f"Error: {filename} not found")
    print(f"Current directory: {os.getcwd()}")


# Error 2
data_file = "data/info.txt"  # Directory doesn't exist
with open(data_file, "r") as file:
    content = file.read()