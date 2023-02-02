a = ("a", 1, True)
print(a)
b = "a", 1, True
print(b)
print("-" * 50)

c = ("hello")
print(type(c))  #this is a string
d = ("hello", )
print(type(d))  #this is a tuple
print("-" * 50)

e = (1, 2, 3)
print(e)
print(e[0])
print(e[1])
print(e[2])
# print(e[3]) IndexError: tuple index out of range
print(e[-1])  #last item
print(e[-2])  #seconf last item
print(e[-3])  #third last item
print("-" * 50)

f = ("a", "b", "c")
# f[0] = "d"
#this is not possible because tuple is  immutable
for i in f:
    print(i)
if "a" in f:
    print("yes")
else:
    print("No")
print("-" * 50)

g = (1, 2, 3, 4, 5, 2, 3, 3, 5, 3)
lenght = len(g)
print(lenght)
print(g.count(3))  # 4
print(g.count(2))  # 2
print(g.count(20))  # 0
print(g.index(2))  #intex of frist apperance of 2 is 1
print(g.index(5))  #4
print("-" * 50)

mylist = [1, 2, 3]
mytuple = tuple(mylist)  # list --> tuple
print(mytuple)
print(type(mytuple))

mylist = list(mytuple)  # tuple --> list
print(mylist)
print(type(mylist))
print("-" * 50)

new_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
new_tuple2 = new_tuple[1:5]
print(new_tuple2)
new_tuple3 = new_tuple[:5]
print(new_tuple3)
new_tuple4 = new_tuple[3:]
print(new_tuple4)
new_tuple5 = new_tuple[::2]
print(new_tuple5)
new_tuple5 = new_tuple[::-1] #this will reverse the tuple
print(new_tuple5)
print("-" * 50)

def details(data):
    name,place,age,good = data
    print(name)
    print(place)
    print(age)
    print(good)
data= "Faheem", "Perinjanam", 20, True
details(data)
print("-" * 50)

def unpacking(data):
    a, *b, c = data
    print(a) #first element 
    print(b) # all elements except first and last
    print(c) #last element
values = (1,2,3,4,5,6)
unpacking(values)
print("-" * 50)

import sys
print(sys.getsizeof(values))
print(sys.getsizeof(list(values)))
print("-" * 50)

