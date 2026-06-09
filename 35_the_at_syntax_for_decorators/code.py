import functools


user = {"username": "Joes", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return "Unauthorized"
        
    return secure_func


@make_secure
def get_password(panel):
    if panel == "admin":
        return "admin123"
    elif panel == "billing":
        return "billing123"



print(get_password("billing"))