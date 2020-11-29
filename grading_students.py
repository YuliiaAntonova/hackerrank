def gradingStudents(grades):
    # Write your code
    return [i if (i < 38 or i % 5 < 3) else (i + (5 - i % 5)) for i in grades]
print(gradingStudents([73,67,38,33]))