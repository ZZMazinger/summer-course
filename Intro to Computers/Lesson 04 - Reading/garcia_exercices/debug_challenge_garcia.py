# Stretch: Debugging Multiple Errors

def calculate_student_grade(scores, student_name):
    total = 0
    global average
    for score in scores:
        total = total + score
    
    average = total / len(scores)
    
    grade_info = {
        "name": student_name,
        "average": average,
        "total": total
    }
    
    if average >= 90:
        grade_info["letter"] = "A"
    elif average >= 80:
        grade_info["letter"] = "B"
    elif average >= 70:
        grade_info["letter"] = "C"
    else:
        grade_info["letter"] = "F"
    
    return grade_info

# Test the function
student_scores = [85, 92, 78, 88]
result = calculate_student_grade(student_scores, "Alice")
print(f"{result['name']} earned a {result['letter']} with an average of {average}")

# Syntax error(s), NameError, KeyError
# 1. KeyError was hardest to identify
# 2. I read the error messages carefully most of the time, but sometimes I just tried to guess
# 3. The line numbers showed where to look for errors
# 4. To debug multiple errors, I ate an elephant one bite at a time