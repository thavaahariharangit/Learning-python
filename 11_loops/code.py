# While Loop
# number = 7

# while True:
#     user_input = input("Would you like to play? (Y/n) ")

#     if user_input == "n":
#         break

#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("you are off by one")
#     else:
#         print("Sorry, It's wrong!")

# friends = ["Rolf", "Jen", "Bob", "Anne"]

# for friend in friends:
#     print(f"{friend} in my friend")


grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(f"average is {total/amount}") 
    