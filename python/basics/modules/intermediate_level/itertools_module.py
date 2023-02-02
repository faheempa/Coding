import operator
from itertools import (
    accumulate,
    combinations,
    combinations_with_replacement,
    count,
    cycle,
    groupby,
    permutations,
    product,
    repeat,
)
import time

a = [1, 2, 5]
b = [3]
prod = product(a, b) # return the cross product
print(list(prod))
print("-" * 50)

premutaions = permutations(a) # returns possible permutations
print(list(premutaions))
print("-" * 50)

comb = combinations(a, 2)  # return possible combinations - (n,r)
print(list(comb))
comb = combinations_with_replacement(a, 2)  # (x,x) is also considered
print(list(comb))
print("-" * 50)
a = [1, 3, 4, 2, 7, 5, 6, 9, 6]
accum = accumulate(a)  # sequential addition
print(a)
print(list(accum))
accum = accumulate(a, func=operator.mul)  # sequential multiplication
print(a)
print(list(accum))
accum = accumulate(a, func=max)  # sequential multiplication
print(a)
print(list(accum))
print("-" * 50)


def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obt = groupby(a, key=smaller_than_3)  # to group by certain condion
for key, value in group_obt:
    print(key, list(value))
group_obt = groupby(a, key=lambda x: x < 3)  # using lambda function
for key, value in group_obt:
    print(key, list(value))
# this will only group elements that are near to each other
print("-" * 50)
# otherwise:
a = [2,6,4,8,1,3,5,7]
grp_ob  = groupby(a,key=lambda x: x<5)
for key,value in grp_ob:
    print(key, list(value))
print("-" * 50)

# example application of groupby
data = [
    {"name": "fahee", "age": 20},
    {"name": "arjun", "age": 20},
    {"name": "soorej", "age": 21},
]
data_group = groupby(data, key=lambda x: x['age'])
for key, value in data_group:
    print(key, list(value))
print("-" * 50)

for i in count(10): #count
    print(i)
    if i == 25:
        break
print("-" * 50)

j=0
a=[1,2,3]
for i in cycle(a): # cycle
    print(i)
    print("---------")
    j+=1
    if j is 9:
        break
print("-" * 50)

for i in repeat(1,5): # repeat
    print(i)