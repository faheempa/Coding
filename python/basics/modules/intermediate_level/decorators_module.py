import functools

from more_itertools import first

def decorator_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        print("A")
        # before:
        result = func(*args, **kargs)
        # after:
        print("C")
        return result

    return wrapper

@decorator_name
def fun1():
    print("B")

fun1()
print("="*50)

# ----------------------------------


def repeat(no):
    def repeator(func):
        @functools.wraps(func)
        def wrapper(*args, **kargs):
            for i in range(no):
            # before:
                result = func(*args, **kargs)
            # after:
            return result
        return wrapper
    return repeator

@repeat(no=5)
def fun2():
    print("faheem")

fun2()
print("="*50)

# ----------------------------------


def first_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        print("start - first_decorator")
        # before:
        result = func(*args, **kargs)
        # after:
        print("stop - first_decorator")
        return result

    return wrapper

def second_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        print("beg - second_decorator")
        # before:
        result = func(*args, **kargs)
        # after:
        print("end - second_decorator")
        return result

    return wrapper

@first_decorator
@second_decorator
def fun3():
    print("hello")

fun3()
print("="*50)

