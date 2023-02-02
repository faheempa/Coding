import random

#  these are psedo random numbers:

# random number between 0 and 1 in float
a = random.random()
print(a)
# random number between 1 and 10 in float
b = random.uniform(1, 10)
print(b)
# random number between 1 and 10 in int, including 1 and 10
c = random.randint(1, 10)
print(c)
# random number between 1 and 10 in int, without including 1 and 10
d = random.randrange(1, 10)
print(d)
# picking a choice
e = ["a", "b", "c", "d"]
f = random.choice(e)
print(f)
# picking a set ofchoice - with no repeatation
g = list("abcdefghijklnmopqrstuvwxyz")
h = random.sample(g, 5)
print(h)
# picking a set ofchoice - with repeatation
i = list("abcdefghijklnmopqrstuvwxyz")
j = random.choices(i, k=5)
print(j)
# shuffling the elements in a list
k = list("abcd")
random.shuffle(k)
print(k)
# reproducing ramdom numbers
random.seed(1)
print(random.random())
random.seed(1)
print(random.random())
print("-" * 50)

# these are real random numbers:

import secrets

# random int value below 10
p = secrets.randbelow(10)
print(p)
# random value from binary 0000 to 1111
q = secrets.randbits(4)
print(q)
# random choice from a list
z = list("abcdefg")
r = secrets.choice(z)
print(r)
print("-" * 50)

# for arrays
import numpy as np

# this will create an array of size 3 with random float values
s = np.random.rand(3)
print(s)
# this will create a 2D array of 3x4 size with random float values - list of list
t = np.random.rand(3, 4)
print(t)
# this will create an array of size 3 with random int values between 1(including 1) and 10(excluding 10)
u = np.random.randint(1, 10, 3)
print(u)
# this will create a 2D array of 3x4 size with random int values between 1(including 1) and 10(excluding 10)
u = np.random.randint(1, 10, (3, 4))
print(u)
# reproducing
np.random.seed(1)
v = np.random.rand(3)
print(v)
np.random.seed(1)
x = np.random.rand(3)
print(x)
