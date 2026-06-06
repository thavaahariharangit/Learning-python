print("06: Advanced Set Operations")

art = {"Bob", "Jen", "Rolf", "Charlie"}
print(f"art's students: {art}")
science = {"Bob", "Jen", "Adam", "Anne"}
print(f"science's students: {science}")


print(f"art's only students: {art.difference(science)}")
print(f"science's only students: {science.difference(art)}")

print(f"art and science students: {art.intersection(science)}")
