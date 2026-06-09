class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # readable, friendly output
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    # detailed, unambiguous output
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
person = Person("Alice", 30)
print(person)      # Output: Alice is 30 years old. str() is called implicitly when we print the object, and it uses the __str__ method to provide a user-friendly string representation of the object.
print(str(person))  # Output: Alice is 30 years old. str is called explicitly, and it also uses the __str__ method to provide the same user-friendly string representation of the object.
print(repr(person)) # Output: Person(name='Alice', age=30) repr is called explicitly, and it uses the __repr__ method to provide a more detailed and unambiguous string representation of the object, which is often used for debugging purposes.