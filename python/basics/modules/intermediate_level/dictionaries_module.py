a={"name": "Faheem", "age":29, "healthy":True}
print(a["name"])
print(a["age"])
print(a["healthy"])
b = dict(name="faheem", age=20, healthy=True) # better
print(a["name"])
print(a["age"])
print(a["healthy"]) 
try:
    print(a["palce"])
except:
    print("'place' is not a key in the a dictionary") 
a["place"]="perinjanam" #adding a key-value pair
print(a["place"]) 
a["place"]="Adoor" # overwritting a key-value pair
print(a["place"]) 
print("-"*50)

print(a)
del a["place"]; # deleting a pair
print(a) 
a.popitem() # poping the last pair
print(a) 
print("-"*50)

if "name" in a: # searching a key-value
    print("yes")
else:
    print("no")
if "dob" in a:
    print("yes")
else:
    print("no")
if "dob" or "name" in a:
    print("yes")
else:
    print("no")
print("-"*50)

for i in b: # looping through keys
    print(i)
for i in b.items(): # looping through key values
    print(i)
for key,value in b.items(): # looping through key and values
    print(key,":",value)
print("-"*50)

original_dic = dict(name="soorej", age=20, healthy=True)
notATrueCopy = original_dic
print(notATrueCopy)
print(original_dic)
notATrueCopy["place"]="kottayam"
print(notATrueCopy)
print(original_dic)

trueCopy=dict(original_dic)
trueCopy["weight"]="55"
print(trueCopy)
print(original_dic)
print("-"*50)

# this will update the existing keys with new values and create new keys they are not already
x=dict(a="A", b=True, c=20, x="dfbawefewffuia") 
y=dict(a="B", b=True, c=25, d="sfssdc")
print(x)
x.update(y)
print(x)
print("-"*50)

# using a tuple as a key
myTuple = (10,5)
sum = dict(myTuple=15) # didnt work
print(sum)
sum = {myTuple:15} # now worked
print(sum)
myTuple2 = (20,10)
sum[myTuple2]=30
print(sum)
print("-"*50)

# using a list as a key
try:
    myList = [10,5]
    sum = {myList:15}
    print(sum)
except:
    print("it doesn't work like that...cant use a list as a key")
print("-"*50)

z= {}
z[1]=2
z[8]=-1
print(z)

