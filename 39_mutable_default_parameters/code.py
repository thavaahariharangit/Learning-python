from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = []): # this is bad
        self.name = name
        self.grades = grades

    def add_grade(self, grade: int):
        self.grades.append(grade)

bob = Student("Bob")
bob.add_grade(90)
print(bob.grades) # [90]

# This is because the default value for grades is shared across all instances of Student.

alice = Student("Alice")
print(alice.grades) # [90] - this is unexpected!