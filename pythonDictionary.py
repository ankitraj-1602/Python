# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

thsidict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1999
}
print(thsidict)
print(thsidict["brand"])
print(len(thsidict))
print(type(thsidict))

# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

thisdict = dict(name="john",age=55)
print(thisdict)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thsidict["brand"])
print(thsidict.get("brand"))

# get Keys
# The keys() method will return a list of all the keys in the dictionary.

print(thisdict.keys())

# Get Values
# The values() method will return a list of all the values in the dictionary.

print(thsidict.values())

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

print(thsidict.items())

thsidict["owner"]="ankit"
print(thisdict)
print("model" in thisdict)

# Change Values
# You can change the value of a specific item by referring to its key name:

thisdict["brand"]="maruti"
print(thisdict["brand"])
thisdict.update({"brand":"suzuki"})
print(thisdict["brand"])

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict["city"]="hazaribagh"
print(thisdict["city"])

# Removing Items
# There are several methods to remove items from a dictionary:

thisdict.pop("city")
thisdict.popitem()
# print(thisdict["city"])
print(thisdict)

# The del keyword can also delete the dictionary completely:
# The clear() method empties the dictionary:

# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

for x in thisdict:
    print(x , end=" ")
    print(thisdict[x], end=" ")
    print()

for x,y in thisdict.items():
    print(x,y)

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

mydict = thisdict.copy()
print(mydict)
mydict2= dict(thsidict)
print(mydict2)


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

mycode = {
    "part1":{
        "code":"python",
        "line":55
    },
    "part2":{
        "code":"c",
        "line":550
    },
    "part3":{
        "code":"js",
        "line":100
    },
}

print(mycode)
print(mycode["part1"]["code"])

for x,obj in mycode.items():
    print(x)

    for i in obj:
        print(i ,obj[i])