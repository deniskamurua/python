import time


# you can use any argument instead of  function but i will use this to remember that am passing a function


def delay_decorator(function):
    def wrapper_function():
        time.sleep(3)

        # Do something before
        # in our case call it twice

        function()
        function()

        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("bye")


def greetings():
    print("Are you okay")


say_bye()
say_hello()


# Advanced decorators
class User:
    def __init__(self, name):
        self.name = name
        self.Is_logged_in = False


def is_authenticated_decolator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

    return wrapper

@is_authenticated_decolator
def create_blog_post(user):
    print(f"This is {user.name}'s blog post")


new_user = User("root")
new_user.Is_logged_in = True
create_blog_post(new_user)
