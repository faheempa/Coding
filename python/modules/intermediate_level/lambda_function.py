from functools import reduce

add10 = lambda x:x+10 # making a function using lambda
print(add10(1))

mult = lambda x,y: x*y # a function that takes 2 parameters
product = mult(2,5)
print(product)
print("-"*50)

points = [(2,3),(15,1),(-1,4),(10,8)]
print(points)
points_sorted_using_lambda = sorted(points,key=lambda x:x[1]) # sorting elements in ascenting order of second values
print(points_sorted_using_lambda)
points_sorted_using_lambda = sorted(points,key=lambda x:sum(x)) # sorting elements using sum
print(points_sorted_using_lambda)
points_sorted_using_lambda = sorted(points,key=lambda x:max(x)) # sorting elements using maximum value of each tuple
print(points_sorted_using_lambda)
points_sorted_using_lambda = sorted(points,key=lambda x:min(x)) # sorting elements using minimum value of each tuple
print(points_sorted_using_lambda)
print("-"*50)

a=[1,2,3,4,5,6]
b=map(lambda x:2*x,a) # map function 
print(a)
print(b)
print(list(b))
c=[x*2 for x in a]
print(c)

d = filter(lambda x: x%2==0, a) # filter function
print(list(d))
e = [x for x in a if x%2==0]
print(e)

product_of_a = reduce(lambda x,y:x*y,a) # reduce function
print(f"product of all elements in a = {product_of_a}")
print("-"*50)



