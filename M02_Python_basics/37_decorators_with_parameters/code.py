import functools


user = {"username": "Joes", "access_level": "guest"}


def makesecure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return "Unauthorized"
        
        return secure_func
    return decorator


@makesecure("admin")
def get_admin_password():
    return "admin123"

@makesecure("guest")
def get_dashboard_password():
    return "dashboard123"


print(get_dashboard_password())
user = {"username": "Joes", "access_level": "admin"}
print(get_admin_password())




