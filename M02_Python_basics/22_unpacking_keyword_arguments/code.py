# kwargs stands for "keyword arguments". It allows you to pass a variable number of keyword arguments to a function. The kwargs parameter is a dictionary that contains all the keyword arguments passed to the function.
# def named(**kwargs):
#     print(kwargs)

# named(name="Bob", age=25, city="New York")

# def named(name, age):
#     print(f"Name: {name}, Age: {age}")

# data = {"name": "Bob", "age": 25}

# named(**data)

# def named(**kwargs):
#     print(f"Name: {kwargs['name']}, Age: {kwargs['age']}")

# data = {"name": "Bob", "age": 25}

# named(**data)

# def named(**kwargs):
#     print(kwargs)

# def print_nicely(**kwargs):
#     named(**kwargs)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_nicely(name="Bob", age=25, city="New York")

def both(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

both(1, 2, 3, name="Bob", age=25)