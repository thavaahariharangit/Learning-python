import functools


user = {"username": "Joes", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)
    def secure_func():
        if user["access_level"] == "admin":
            return func()
        else:
            return "Unauthorized"
        
    return secure_func


@make_secure
def get_admin_password():
    return "admin123"



print(get_admin_password())
user = {"username": "Joes", "access_level": "admin"}
print(get_admin_password())

print(get_admin_password.__name__)