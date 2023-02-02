import numpy as np

arr = np.array([5, 2, 1, 3, 4])
arr2 = np.array([[6, 4, 5], [1, 3, 2]])
arr3 = np.array([True, False, True, True, False])
arr4 = np.array(["efg", "abcd", "lmn", "hijk", "opqr"])

# sorting
print(np.sort(arr))
print(np.sort(arr2))
print(np.sort(arr3))
print(np.sort(arr4))

# this will return index of values to placed, to be order
arr5 = np.array([1,2,3,5,7,8])
print(np.searchsorted(arr5,4))
print(np.searchsorted(arr5,[4,6,9]))

