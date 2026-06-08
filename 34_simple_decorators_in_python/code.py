user = {"username": "Joes", "access_level": "guest"}

def get_admin_password():
    return "admin123"

def make_secure(func):
    def secure_func():
        if user["access_level"] == "admin":
            return func()
        else:
            return "Unauthorized"
        
    return secure_func



get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
user = {"username": "Joes", "access_level": "admin"}
print(get_admin_password())