a = []
b = a

print(id(a)) # 140353913896448
print(id(b)) # 140353913896448

a.append(1)

print(a) # [1]
print(b) # [1]

c = []
d = []

print(id(c)) # 125915885404032
print(id(d)) # 125915887868864

c.append(1)

print(c) # [1]
print(d) # []


e = 1
f = 1

print(id(e)) # 9793216
print(id(f)) # 9793216

e = 2
print(id(e)) # 9793248
print(id(f)) # 9793216

a = "Hello"
b = a

a += " World"

print(a) # Hello World
print(b) # Hello