# lists
# ordered
l = ["Bob", "Rolf", "Anne"]
print(l[1]) # indexing with order

l[0] = "Smith"
print(l)

# add
l.append("Bob")
print(l)

#  tuple
t = ("Bob", "Rolf", "Anne")
print(t[2]) # indexing with order

# t[0] = "Smith" # tuple cannot be modified
print(t)

#  set
#  unique values
#  order is not respected
s = {"Bob", "Rolf", "Anne"}
print(s)
s.add("David")
print(s)

