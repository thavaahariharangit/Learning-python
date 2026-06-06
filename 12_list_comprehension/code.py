numbers = [1, 3, 5]


#  Traditional way
# doubled = []
# for number in numbers:
#     doubled.append(number * 2)

doubled = [num * 2 for num in numbers]

print(doubled)

friends = [ "Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

# Traditional way
# list = []
# for friend in friends:
#     if friend.startswith("S"):
#         list.append(friend)

list = [f for f in friends if f.startswith("S")]

print(list)