import numpy as np

arr = np.array([1,2,3,4])
print(arr)

zero_dim = np.array(1)
one_dim = np.array([1,2,3,4,5])
two_dim = np.array([[1,2,3],[4,5,6],[7,8,9]])
three_dim = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print(zero_dim)
print(one_dim)
print(two_dim)
print(three_dim)
print(zero_dim.ndim)
print(one_dim.ndim)
print(two_dim.ndim)
print(three_dim.ndim)

# this will create a 3d array
new_array = np.array([1,2,3], ndmin=3)
print(new_array)
print("-"*50)

print(one_dim[0])
print(one_dim[1])
print(two_dim[0])
print(two_dim[0,0])
print(two_dim[0,2])
print(three_dim[0,0,0])

# slicing
print(one_dim[0:3])
print(one_dim[1:])
print(one_dim[:3])
print(one_dim[:])
print(one_dim[-1])
print(one_dim[-1:])
print(one_dim[0:4:2])
print(one_dim[::-1]) # reverse
print(two_dim[0,0:]) # first list
print(two_dim[1,0:]) # second list
print(two_dim[0,0:1]) # first element in first list
print(two_dim[0:2]) # first 2 lists
print(two_dim[0:]) # complete 2d array
print(two_dim[0:,0]) # first element from each list
print(two_dim[0:,1]) # second element from each list
print(two_dim[0:,0:2]) # first and second element from each list
# [starting_list_index : ending_list_index , starting_element : end_element]
print("-"*50)

# copy
arr = one_dim.copy()
one_dim[0]=100
print(one_dim)
print(arr)

# veiw
arr2 = one_dim.view()
one_dim[0]=1000
print(one_dim)
print(arr2)

# checking whether an arr is copy or view
print(arr.base) # copy - none
print(arr2.base) # view - will be an array
print("-"*50)

print(two_dim)
print(two_dim.shape)
print(two_dim.reshape(1,9))
print(two_dim.reshape(9,1))
arr3 = np.array([1,2,3,4,5,6,7,8,9])
print(arr3.reshape(3,3))
try:
    print(arr3.reshape(3,4))
except:
    print("cant reshape")

# returns the number of trues
a=np.array([0,1,1,0,0,0,1,0])
b=np.array([0,1,0,0,1,0,1,1])
print(np.sum(a==b))









