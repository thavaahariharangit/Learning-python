def add(x, y):
    return x + y

result = add(5, 8)
print(result)

# 2 returns in on function
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "you fool!"
    
print(divide(5,0) * 3)
print(divide(15,3) * 3)