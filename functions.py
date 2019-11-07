def my_decorator(func):
    def wrapper():
        print("Happening before function call.")
        func()
        print("Happening after function call.")
    return wrapper


@my_decorator
def say_something():
    print("Mercredi soir c'est Barbu")

wrapper = my_decorator(say_something)
wrapper()
