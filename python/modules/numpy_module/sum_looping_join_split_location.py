import numpy as np

a = np.array([1,4,9,16])
b = np.array([10,20,30,40])
print(a+b)
print(b-a)
print(a*b)
print(a/b)
print(a//b)
print(a**2)
print(a**0.5)
print(np.sqrt(a))

c=np.arange(1,5)
print(c)
d=np.arange(5)
print(d)

print(c*2)
print(c**c)

e=np.array([2,5,3,7,9])
print(e > 3)
print("-"*50)

arr = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],
                 [4,5,6]])
print(sum(arr))
print(sum(arr2)) # [1+4 , 2+5 , 3+6]
print(arr.sum())
print(arr2.sum())
print(arr.min())
print(arr.max())
print(arr2.max())

# add elements in an array by row
print(arr2.sum(axis=1))
# add elements in an array by column
print(arr2.sum(axis=0))
print("-"*50)

for n in arr:
    print(n)
for n in arr2:
    print(n)
for n in arr2:
    for m in n:
        print(m)
print()

# better way
for e in np.nditer(arr2):
    print(e)
print()
for i,n in np.ndenumerate(arr2):
    print(f"element at {i} is {n}")
print()

# concatination/join
print(np.concatenate((a,b)))
arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[7,8,9],[10,11,12]])
print(np.concatenate((arr3,arr4)))
print(np.concatenate((arr3,arr4), axis=1)) # joining row to row

# array split
arr5 = np.array([1,2,3,4,5,6,7,8])
arr6 = np.array_split(arr5,4)
print(arr5)
print(arr6)
tuple_of_arrays = tuple(arr6)
p,q,r,s = tuple_of_arrays
print(p)
print(q)
print(r)
print(r)
print(s)
print("-"*50)

# locating an element
arr7 = np.array([1,3,2,3,4,5,2,6,7,4,8,3])
loc = np.where(arr7 == 3)
print(loc)
loc = np.where(arr7 == 4)
print(loc)
# location of elements that are less than 5
loc = np.where(arr7 < 5)
print(loc)
# location of elements that are divisible by 3
loc = np.where(arr7 % 3 == 0)
print(loc)
print(type(loc))