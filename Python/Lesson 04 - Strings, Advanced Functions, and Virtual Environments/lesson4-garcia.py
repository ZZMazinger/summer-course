# # Strings Practical Exercise #1 - Username Validator
# # Input: username
# # Output: validation

# # Define validate function
# def validate_username(username: str) -> bool:
#     digit_counter = 0

#     for character in username:
#         if character.isdigit():
#             digit_counter += 1

#     if len(username) < 5 or len(username) > 15:
#         return False
#     elif not username.replace('_', '').isalnum():
#         return False
#     elif not username[0].isalpha():
#         return False
#     elif username.endswith('_'):
#         return False
#     elif digit_counter == 0:
#         return False
#     else:
#         return True

# # Assertion
# assert validate_username('testcase_123') == True

# # Test Cases
# print(validate_username("coder_42"))
# print(validate_username("2cool"))
# print(validate_username("hi"))
# print(validate_username("python_dev_"))
# print(validate_username("justletters"))


# Strings Practical Exercise #2 - Secret Message Decoder
# Input: spy message
# Output: decoded message

# # Define a decoder function
# def decode(message: str) -> str:
#     message = message[::-1]
#     message = message.replace("#", " ")
#     message = message.replace("0", "")
#     message = message.replace("1", "")
#     message = message.replace("2", "")
#     message = message.replace("3", "")
#     message = message.replace("4", "")
#     message = message.replace("5", "")
#     message = message.replace("6", "")
#     message = message.replace("7", "")
#     message = message.replace("8", "")
#     message = message.replace("9", "")
#     message = message.split(" ")
#     message = message[::-1]
#     message = " ".join(message)
#     message = message.capitalize()
#     return message

# # Call the function
# print(decode("eht7#terces#3edoc#si#nohtyp9"))

# # This was not the most efficient way to do it, but it works


# # Functions with multiple returns practical
# # Input: Passengers list
# # Output: seat numbers

# # Define function to make use of enumerate()
# def print_boarding_list(passengers):
#     for seat, passenger in enumerate(passengers):
#         print(f"Seat {seat +1}: {passenger}")

# passengers = ["Lopez", "Chen", "Okafor", "Smith", "Patel"]

# print_boarding_list(passengers)

# # Note that you can also pass a second argument to enumerate() to designate the starting value instead of doing the +1 like I did


# # Functions with default parameters practical exercise
# # Input: list of grades
# # Output: list of curved grades

# # Define the function
# def curve_grades(scores, bonus=5, max_score=100):
#     new_scores = []
#     for grade in scores:
#         grade = grade + bonus
#         if grade > max_score:
#             grade = max_score
#         new_scores.append(grade)
#     return new_scores

# # Given grade list
# grade_list = [88, 97, 75]

# # Call the function
# print(curve_grades(grade_list))