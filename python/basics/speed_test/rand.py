import functools
import time
def get_run_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        for _ in range(1000):
            func(*args, **kargs)
        end = time.time()
        return f'Run Time of {wrapper.__name__} : {round((end - start) * 10**3, 2)} ms'
    return wrapper

@get_run_time
def isPrime1(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


@get_run_time
def isPrime2(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False

    return True


from math import sqrt

@get_run_time
def isPrime3(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False

    return True


print(isPrime1(113))
print(isPrime2(113))
print(isPrime3(113))