import json

a = dict(
    name="faheem",
    age=20,
    address=(
        "poovamparambil house",
        "s/o Abdul Rasheed",
        "p.o.perinjanam",
        "pincode:680686",
    ),
    healthy=True,
    hobbies=["coding", "entainment media", "learning"],
    dob=dict(dd=24, mm=5, yy=2002),
    problems=None,
)

# encoding to a json file
with open("file_for_json.json", "w") as file:
    f = json.dump(a, file, indent=4, sort_keys=True)
print("dictionary exported as a json file")
print("-" * 50)


# returning the json file as string
a_json = json.dumps(a, indent=4, sort_keys=True)
print(a_json)
print("-" * 50)


# decoding back to python
b = json.loads(a_json)
print(b)
print("-" * 50)


# decoding from the file
with open("file_for_json.json", "r") as file2:
    c = json.load(file2)
    print(c)
print("-" * 50)


# encoding an object
class User:
    def __init__(self, name, age, healthy):
        self.name = name
        self.age = age
        self.healthy = healthy

user1 = User("fahee", 20, True)
# we cant directy convert to json. so we use a custom function which return a dictionary
def obj_to_json(obj):
    if isinstance(obj, User):
        return dict(name=obj.name, age=obj.age, healthy=obj.healthy, class_name=obj.__class__.__name__)
    else:
        raise TypeError("Object of type User is not JSON serializable")

user1_json = json.dumps(user1, default=obj_to_json)
print(user1_json)
print("-" * 50)


#decoding back to class object
def dict_to_obj(dict):
    if User.__name__ == dict["class_name"]:
        return User(dict["name"],dict["age"],dict["healthy"])
    else:
        print("cant convert to an object")
        return dict

user_as_object = json.loads(user1_json, object_hook=dict_to_obj)
print(type(user_as_object))
print(user_as_object.name)
print(user_as_object.age)
print(user_as_object.healthy)