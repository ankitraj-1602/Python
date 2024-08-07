# Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
#  Note: Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

sets = {"a","b","c",33,"a"}
print(sets)
print(len(sets))
print(type(sets))

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword

for x in sets:
    print(x)

# To add one item to a set use the add() method.

sets.add("rr")
print(sets)

sets2 = {"rahul"}
sets.update(sets2)
print(sets)
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

sets.remove("rahul")
print(sets)
sets.discard("rahul")
print(sets)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

# Loop Items
# You can loop through the set items by using a for loop:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join Sets
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the uplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.