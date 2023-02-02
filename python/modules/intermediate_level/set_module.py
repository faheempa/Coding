set1 = {1, 2, 3, 4, 5}
print(set1)
set2 = {1, 2, 3, 4, 2, 4, 5, 1, 2}  # no duplicates allowed
print(set2)
set3 = set("faheem")  # unordered and no duplicates
print(set3)
set4 = set()  # creating an empty set
print(type(set4))
print(set4)
print("-" * 50)

set4.add(1)  # adding elements to the set
set4.add(3)
set4.add(2)
set4.add(4)
print(set4)  # order of values is not considered
set4.remove(3)  # removing an element from set
set4.remove(1)
print(set4)
print("-" * 50)

try:
    set4.remove(20)  # 20 is not present in the set
except:
    print("Element not found")
    print(set4)
set4.add(10)
set4.add(15)
print(set4)
set4.discard(10)  # another method to delete an elemrnt from set
print(set4)
try:
    set4.discard(20)
    # even tho 20 is not an elemnt in the set, it doesnt give an error
    print(set4)
except:
    print("Element not found")
value = set4.pop()  # to pop an element from the set
print(value)
print(set4)
set4.clear()  # this will clear the set
print(set4)
print("-" * 50)

for i in set1:  # looping through the setW
    print(i)
if 3 in set1:  # searcing in a set
    print("yes")
if 10 in set1:
    print("yes")
else:
    print("NO")
print("-" * 50)

even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9, 11}
prime = {2, 3, 5, 7, 11, 13}
unionOfOddAndEven = odd.union(even)  # union function - no duplicates
print(unionOfOddAndEven)
intersectionOfOddAndPrime = odd.intersection(prime)  # intersection
print(intersectionOfOddAndPrime)
intersectionofOddAndEven = odd.intersection(even)
print(intersectionofOddAndEven)
oddValuesThatAreNotPrime = odd.difference(prime)  # set difference
print(oddValuesThatAreNotPrime)
print("-" * 50)

set5 = {1, 2, 3, 4, 5}
set6 = {1, 2, 6, 7, 8}
uniqueValuesInBothSets = set5.symmetric_difference(
    set6
)  # (a union b) - (a intersection b)
print(uniqueValuesInBothSets)
print("-" * 50)

set7 = {1, 2, 3, 4, 5, 6}
set8 = {1, 3, 5, 7, 8, 9, 10}
print(set7)
set7.update(set8)  # updates the set with all values from both set
print(set7)
set7.intersection_update(set8)
# updates the set with common values from both set
print(set7)
set7.add(20)
set7.difference_update(set8)
print(set7)
set7.symmetric_difference_update(set8)
print(set7)
print("-" * 50)

set9 = {1, 2, 3, 4, 5, 6}
set10 = {1, 2, 3}
print(set9.issubset(set10))  # false
print(set10.issubset(set9))  # true
print(set9.issuperset(set10))  # true
print(set10.issuperset(set9))  # false
print(set9.isdisjoint(set10))  # false
set11 = {10, 15, 20}
print(set9.isdisjoint(set11))  # true
print("-" * 50)

# coping a set
set12 = set(set10)
print(set12)
print(set10)
print("-" * 50)

set13 = set([1, 2, 3, 4, 5])  # normal set
print(set13)
set14 = frozenset([5, 10, 15])  # frozen set - it is like a constant
print(set14)
try:
    set14.add(20)
except:
    print("cant add elements to frozen set")
try:
    set14.update(set1)
except:
    print("cant update elements to frozen set")
try:
    set14.remove(set1)
except:
    print("cant remove elements to frozen set")
try:
    set14.clear()
except:
    print("cant clear the frozen set")
try:
    set15 = set14.union(set10)
    print(set15)
    print(
        "we can perform union operation on frozen set and the output set is also a frozen set"
    )
except:
    print("cant perform this operation")
