# function defined with parameters
def add(x, y):
    result = x + y
    print(result)

# function called with arguments
add(5, 3)


# Postional arguments/ parameters
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

# Postional arguments
say_hello("Bob", "Smith")

#  keyword or named arguments
say_hello(surname="Bob", name="Smith")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool!")

divide(dividend=15, divisor=0)