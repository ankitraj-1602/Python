# Python Variables
# Variables
# Variables are containers for storing data values.

# Creating Variables
# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)
x='a'
print(x)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x=int(4)
y=str(4)
z=float(4)
print(type(x),type(y),type(z))

# Camel Case - myVariableName = "John"
# Pascal Case - MyVariableName = "John"
# Snake Case - my_variable_name = "John"

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)


# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"
y=3

def myfunc():
  x = "fantastic"
  y=4
  print("Python is " + x, y)

myfunc()

print("Python is " + x, y)

# to update global variable inside funciton 

x=5

def myfun():
  global x
  x=66
  print(x)
myfun()

