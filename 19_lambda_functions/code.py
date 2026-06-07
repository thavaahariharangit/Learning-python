# add = lambda x,y: x + y
# print(add(5,8))

# print((lambda x,y: x + y)(5, 8))

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
# doubled = [ double(x) for x in sequence]
doubled = map(lambda x: x * 2, sequence)
print(doubled)