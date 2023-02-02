# a= 5+"10" #type error

# import faheem # module not found error

# a=b # name error

# f=open("somefile.txt")# file not found error

# a=[1,2,3]
# a.remove(4) # value erroe

# dictionary = dict(name="fahee")
# dictionary["age"] # key error

x = int(input("enter a value: "))
if x == 5:
    raise Exception("x shouldn't be 5")
    # raising an exception when the condition is true

assert x >= 0, "x is not positive"
# raising an assertion error

try:
    a = 10 / 5
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine")
# if no exception occurs, else block is exicuted
finally:
    print("finaly block is called")
# finally block is always exicuted

# user defined error - 1
class valueTooHightError(Exception):
    pass


# user defined error - 2
class valueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test(x):
    if x > 100:
        raise valueTooHightError(" value is too high")
    if x < 10:
        raise valueTooSmallError("value is too small :", x)


try:
    b = 5
    test(b)
except valueTooSmallError as e:  # e is an object of our error class
    print(e.message, e.value)

try:
    a = 200
    test(a)
except valueTooHightError as e:
    print(e)
