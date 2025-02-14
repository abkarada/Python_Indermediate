"""def mydecorator(function):

    def wrapper(*args, **kwargs):
       # print("I am decorating your function!")
        function(*args, **kwargs)
        print("I am decorating your function!")
    return wrapper


@mydecorator
def hello_world(person):
    print("Hello {person}!")

#mydecorator(hello_world)()
hello_world("mike")
"""
#Practical Example #1 - Logging

import time

def logged(function):
    def wrapper(*args, **kwargs):
        print(f"Function {function.__name__} was called at {time.ctime()}")
        result = function(*args, **kwargs)
        return result
    return wrapper

@logged
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")