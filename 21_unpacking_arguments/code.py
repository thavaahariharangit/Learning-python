# def multiply(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result

# print(multiply(2, 3, 4))  # Output: 24

def add(x, y):
    return x + y

# numbers = (3, 5)
# print(add(*numbers))  # Output: 8

# numbers = { "x": 3, "y": 5 }
# print(add(**numbers))  # Output: 8

def calculate(*args, operation):
    if operation == "add":
        return sum(args)
    elif operation == "subtract":
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "divide":
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    else:
        raise ValueError("Invalid operation")
