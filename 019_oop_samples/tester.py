def wrapper(func):
    def inner():
        print('Starting!')
        func()
        print('Ending!')
    return inner


@wrapper
def say_hello():
    print('Hello world!')

say_hello()

@wrapper
def squares(num):
    print(num ** 2)

