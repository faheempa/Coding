import collections
from collections import defaultdict, deque, namedtuple, Counter

# counter
var = "asdasdfsdfaasfssdadasf"
my_counter = Counter(var)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))  # key-value pair
print(my_counter.most_common(1)[0][0])  # key
print(my_counter.most_common(1)[0][1])  # value
print(my_counter.most_common(2))
print(list(my_counter.elements()))
my_counter["f"] -= 4  # reducing the count of f by 4
print(my_counter)
print("-" * 50)

# namedtuple
Point = collections.namedtuple("Point", ["x", "y"])
pt = Point(2, 5)
print(pt)
print(pt.x)
print(pt.y)
print("-" * 50)

# defualt-dictionary
my_dictionary = defaultdict(int)  # defualt value of int is 0
my_dictionary["a"] = 1
my_dictionary["b"] = 2
print(my_dictionary["a"])
print(my_dictionary["b"])
print(my_dictionary["c"])  # in normal dictionary this will rise a keyerror, but not in defualt-dictionary
print("-" * 50)

# deque
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([2,4,6,8,10,2,4,2])
print(d)
# d.appendleft([2,33,45,2])
# print(d)
print(d.count(2))
print(d.index(10))
d.rotate(1)
print(d)
d.rotate(2)
print(d)
d.rotate(-1)
print(d)
e = d.copy()
print(e) 
