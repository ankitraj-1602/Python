# Tuple
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuple items are ordered, unchangeable, and allow duplicate values and indexed.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

print(len(thistuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tpl = ("ak",1, "a k", 55)
print(type(tpl))

tpl2= tuple(("ar", 1,2,3,"aa  rr"))

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:
print(tpl[2])
print(tpl[-1])
print(tpl[1:4])
print('ake' in tpl)

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# delete tuple
del thistuple
# print(thistuple)

# Unpacking a Tuple
# we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry")
(a,b,c)=fruits
print(a,b,c)

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

(a,*b)=fruits
print(a,b)
(*a,b)=fruits
print(a,b)

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

for x in fruits:
    print(x,end=" ")
for i in range(len(fruits)):
    print(fruits[i],end=" ")

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

print(mytuple.count('apple'))
print(mytuple.index('apple'))