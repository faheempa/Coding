def my_generator():
    yield 7
    yield 20
    yield 6


a = my_generator()
print(list(a))

b = my_generator()
value = next(b)  # this will run the generator until the next yield
print(value)
value = next(b)
print(value)
value = next(b)
print(value)
try:
    value = next(b)
    print(value)
except:
    print("Out of bound - no more to yield")

c = my_generator()
print(sum(c))

d = my_generator()
print(sum(c))
print(sorted(d))

e = my_generator()
print(sorted(e))
print(sum(e))
# this will be zero because e is already generated and used by sorted fuction
print("=" * 50)

import sys


def firstn_fun(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sum(firstn_fun(10)))
print(sum(firstn_generator(10)))

print(sys.getsizeof(firstn_fun(1000)))
print(sys.getsizeof(firstn_generator(1000)))
print("=" * 50)


def fibonacci_generator(l):
    a, b = 0, 1
    while a < l:
        yield a
        a, b = b, a + b

print(list(fibonacci_generator(10)))
print(sys.getsizeof(fibonacci_generator(10)))
print("=" * 50)

mylist_using_generator = (i for i in range(50) if i%2==0)
mylist_using_listcomprehenstion = [i for i in range(50) if i%2==0]
print(list(mylist_using_generator))
print(mylist_using_listcomprehenstion)
print(sys.getsizeof(mylist_using_generator))
print(sys.getsizeof(mylist_using_listcomprehenstion))


