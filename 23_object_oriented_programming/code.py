# student = {"name": "Jose", "school": "Computing", "grades": (66, 77, 88)}

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student["grades"]))

class Student:
    def __init__(self, name, school, grades):
        self.name = name
        self.school = school
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)
    
student = Student("Jose", "Computing", (66, 77, 88))
print(student.name)
print(student.average())