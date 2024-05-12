def authorization_required(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if check_permission(permission):
                return func(*args, **kwargs)
            else:
                update_security_log('Unauthorized access attempt')
                return 'Unauthorized Access'
        return wrapper
    return decorator

def check_permission(permission):
    authorized_users = ['Alice', 'Bob', 'Charlie']
    return permission in authorized_users

def update_security_log(message):
    print(f'Security Log: {message}')

@authorization_required('admin')
def admin_task():
    return 'Admin Task Executed'

@authorization_required('user')
def user_task():
    return 'User Task Executed'

print(admin_task())
print(user_task())
