users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4ssword"),
    (3, "username", "123")
]

username_mapping = {user[1]: user for user in users}

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

_, username, password = username_mapping[input_username]
if password == input_password:
    print("Success")
else:
    print("Failed")