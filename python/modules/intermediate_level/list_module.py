
a = [1,2,3]
print(a)
a[0]=10
print(a)
a = [3,4,5,6]
print(a)
print("-"*50)

b = list() #creating an empty list
print(b)
b.append("hello")
print(b)
print(b[0])
print("-"*50)

c = [1, "a", True, 'hello']
print(c)
print("-"*50)

for i in c:
    print(i) 
print("-"*50)

if "hello" in c: #seacrhing an element
    print("yes")
else:
    print("No")
print("-"*50)

length = len(c)
print(length)
print("-"*50)

d = [13,2,31,40,6]
print("before: ",d)
d.insert(3, 5)
print("inserting 5: ",d)
d.append(7)
print("appending 7: ",d)
d.remove(2)
print("removing 2: ",d)
d.reverse()
print("reverse order: ",d)
new_list = sorted(d)
print("new sorted list:", new_list) # creating a new sorted list 
print("original list: ",d)
d.sort()                            # sorting the existing list
print("sorted: ",d)
# d.remove(20) # this will show error
d.clear()
print("all cleared: ",d)
print("-"*50)

e = [0]*5 
print(e)
e = [0,1]*5
print(e)
e = [0,"hello"]*5
print(e)
print("-"*50)

f=[1,2,3,4]
g=[4,5,6]
h=f+g
print(h)
print("-"*50)

i=[1,2,3,4,5,6,7,8]
j=i[2:5] #starting:stoping intex
print(j)
k=i[:5]  #without starting intex
print(k)
l=i[4:]  #without stoping intex
print(l) 
m=i[::1] #take values from beg to end at a step of 1
print(m)
n=i[::2] #step 2
print(n)
print("-"*50)

original_list = ["a","b","c","d"]
not_a_true_copy_of_list = original_list
not_a_true_copy_of_list.append("e")
print(original_list)
print(not_a_true_copy_of_list)
# e got appented to both lists
true_copy_of_list = list(original_list)
true_copy_of_list.append("e")
print(original_list)
print(true_copy_of_list)
print("-"*50)

values = [1,2,3,4,5]
square_values = [i*i for i in values] # syntax: expression for_in_loop
print(values)
print(square_values)


# count
print(values.count(2))