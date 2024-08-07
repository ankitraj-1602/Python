# Strings

# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a= """
hello 
ankit 
raj how 
are u

"""
# print(a)

# Strings are Arrays

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

line= "hello raj"
print(line[4])

for s in line:
    print(s)
print(len(line))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("f" in txt)

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

print("f" not in txt)


# Slicing

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

b='hello raj'
print(b[1:4])
print(b[:4])
print(b[1:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

b = "Hello, World!"
print(b[-5:-2])
print(b[8:11])

print(b[::-1]) #reverse string