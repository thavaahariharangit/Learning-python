# class ClassTest:
#     def instance_method(self):
#         print(f"This is an instance method of {self}")
    
#     @classmethod
#     def class_method(cls):
#         print(f"This is a class method of {cls}")
    
#     @staticmethod
#     def static_method():
#         print("This is a static method.")

# test = ClassTest()
# test.instance_method()  # This is an instance method of <__main__.ClassTest object
# ClassTest.instance_method(test)  # This is an instance method of <__main__.ClassTest object

# ClassTest.class_method()  # This is a class method of <

# ClassTest.static_method()  # function placed inside the cass, but it does not have access to the class or instance.

# instance methods are used to access and modify the state of an instance, 
# class methods are used to access and modify the state of the class
# static methods are used for utility functions that do not need access to the class or instance.


class Book:
    TYPES = ("hardcover", "paperback", "ebook")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}kg>"
    
    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight)
   
print(Book.TYPES)  # ('hardcover', 'paperback', 'ebook')
book = Book("The Great Gatsby", "hardcover", 1.5)
print(book)  # The Great Gatsby

hardcover_book = Book.hardcover("To Kill a Mockingbird", 1.2)
print(hardcover_book)  # To Kill a Mockingbird