s1 = 'Faheem'
print(s1)
s2 = "Faheem"
print(s2)
s4 = "I'm faheem"
print(s4)
s5 = "I'm faheem"
print(s5)
s6 = """hi, 
im faheem
nice to meet you..."""  # multiline string
print(s6)
s7 = """hi, \
im faheem... \
nice to meet you..."""  # multiline string but in a single line
print(s7)
print("-" * 50)

firstChar = s1[0]  # f
secondChar = s1[1]  # a
print(firstChar)
print(secondChar)
lastChar = s1[-1]  # m
secondLastChar = s1[-2]  # e
print(lastChar)
print(secondLastChar)
print("-" * 50)

try:
    s1[0] = "F"
except:
    print("string is immutable")

s7 = "HEllO_WORLD"
s8 = s7[0:5]
print(s8)
s9 = s7[:5]
print(s9)
s10 = s7[6:]
print(s10)
s11 = s7[::1]
print(s11)
s12 = s7[::2]
print(s12)
s13 = s7[::-1]
print(s13)
print("-" * 50)

str1 = "hello"
str2 = "world"
str3 = str1 + " " + str2
print(str3)
if "w" in str1:
    print("yes")
else:
    print("no")
if "h" in str1:
    print("yes")
else:
    print("no")
print("-" * 50)

str4 = "   faheem    "
print(str4)
str4 = str4.strip()
print(str4)
str4 = str4.upper()
print(str4)
str4 = str4.lower()
print(str4)
print("-" * 50)

print(str3)
print(str3.startswith("h"))
print(str3.startswith("hello"))
print(str3.startswith("hey"))
print(str3.endswith("world"))
print(str3.endswith("wood"))
print(str3.find("l"))
print(str3.find("orld"))
print(str3.find("nothing"))
print(str3.count("e"))
print(str3.count("l"))
print(str3.replace("world", "india"))
print("-" * 50)

#  string to list
myString = "this is a string test 1"
print(myString)
myList = myString.split() # by defualt it splits the string at each space
print(myList)
myString = "this_is_a_string_test_2"
print(myString)
myList = myString.split("_") # it splits the string at each underscore
print(myList)
print("-" * 50)

# list to string
print(myList)
new_string = "".join(myList) # dot joint method
print(new_string)
new_string = " ".join(myList) # seperator is given inside ""
print(new_string)
print("-" * 50)

# formatting methods
# using %
var1 = "faheem"
var2 = 20
print("hey...this is %s..im %d" % (var1,var2))
# using format
print("hey...this is {name}..im {age}".format(name=var1,age=var2))
print("hey...this is {}..im {}".format(var1,var2))
print("hey...this is {1}..im {0}".format(var1,var2))
# using f-string
print(f"hey...this is {var1}..im {var2}")
print("-" * 50)


a = [1,2,3,4]
def func():
    return list("asdf")
a = func()
print(a)

x=1
y=2
z=str(x*10+y)
print(type(z))
print(z)