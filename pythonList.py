# List

# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:
# mylist = ["apple", "banana", "cherry"]

# List Items
# List items are ordered, changeable, and allow duplicate values and indexed.

listItems = [1,'ankit','raj ', 44]
print(listItems)
print(len(listItems))
print(type(listItems))

listItems2 = list((1,'ankit'))
print(listItems2)
print(type(listItems2))


# MOST IMPORTANT
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access List Items

# List items are indexed and you can access them by referring to the index number:

print(listItems[2])
print(listItems[-1])
print(listItems[1:3])
# When specifying a range, the return value will be a new list with the specified items.
print(listItems[-2:-1])
print('ankit' in listItems)


# Change List Items

# To change the value of a specific item, refer to the index number:
listItems[1]='python'
print(listItems)

listItems[1:3] = ["snake","anaconda"]
print(listItems)

listItems[1:3] = ['a']
print(listItems)
# The length of the list will change when the number of items inserted does not match the number of items replaced.

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:

listItems.insert(0,'abc')
print(listItems)

# Add List Items

# Append Items
# To add an item to the end of the list, use the append() method:

listItems.append('ankit raj')
print(listItems)

# Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:

listItems.insert(0,'ankit raj')
print(listItems)

# Extend List
# To append elements from another list to the current list, use the extend() method.

listItems.extend(listItems2)
print(listItems)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Remove List Items
# The remove() method removes the specified item
# If there are more than one item with the specified value, the remove() method removes the first occurrence:

# listItems.remove('a raj')
print(listItems)

# Remove Specified Index
# The pop() method removes the specified index.
listItems.pop()
print(listItems)

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.

lst = ['a','r',4]
print(lst)
lst.clear()
print(lst)

# Loop Through a List
# You can loop through the list items by using a for loop:

for x in listItems:
    print(x,end=" ")
for i in range(len(listItems)):
    print(listItems[i],end=" ")

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
# A short hand for loop that will print all items in a list:

[print(x) for x in listItems]

# List Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

l=['ankit raj' ,'a', 'raj']
newList = [x for x in l if "j" in x]
print(newList)

# Sort Lists
# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

l.sort() #inplace sorting no new list created 
print(l)
l.sort(reverse=True)
print(l)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
thislist.reverse()
print(thislist)

# Use the copy() method
# You can use the built-in List method copy() to copy a list.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Use the list() method
# Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#another way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)