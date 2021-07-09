def first_decorator(func):
    def wrapper():
        print('hello world')
        func()
        print('hello world')
    return wrapper


@first_decorator
def add():
    print(10)

add()