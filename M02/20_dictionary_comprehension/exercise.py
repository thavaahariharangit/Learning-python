student = {
    "name": "Jose",
    "school": "Computing",
    "grades": (66, 77, 88)
}

def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)

print(average_grade(student))

student_list = [
    { "name": "Jose", "school": "Computing", "grades": (66, 77, 88) },
    { "name": "Bob", "school": "Arts", "grades": (82, 85, 92) },
    { "name": "Rolf", "school": "Science", "grades": (66, 68, 75) },
]

def average_grade_all_students(students):
    total = 0
    grade_count = 0
    for student in students:
        grades = student["grades"]
        total += sum(grades)
        grade_count += len(grades)
    return total / grade_count

print(average_grade_all_students(student_list))