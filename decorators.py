# Decorators are a way to wrap another function 
# by extending behaviour of the wrapped function, 
# without permanently modifying the it.

import functools

def log_execution(func):
    @functools.wraps(func) # This wrapper from functools module preserves the function's metadata(like name, docstring, etc)
    def wrapper(*args, **kwargs):
        print(f'Name of the function being called: {func.__name__} with arguments:', *args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_execution
def say_hello(name: str) -> str:
    '''This function says hello'''
    return f'Hello, {name}!'

print('Prints related to wrapper with functools.wraps()')
print(say_hello.__name__)
print(say_hello.__doc__)
print(say_hello.__annotations__)
print(say_hello.__module__)

def simplewrap(func):
    def wrapper(*args, **kwargs):
        print(f'Name of the function being called: {func.__name__} with arguments:', *args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@simplewrap
def say_bye(name: str) -> str:
    '''This function says bye'''
    return f'Bye, {name}!'

print('Prints related to wrapper with functools.wraps()')
print(say_bye.__name__)
print(say_bye.__doc__)
print(say_bye.__annotations__)
print(say_bye.__module__)

# Except for the difference in losing metadata of the original function, both wrapper have done their jobs.
say_hello('Shivu')
say_bye('Kavya')