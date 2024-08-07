# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

txt = "We are the so-called \"Vikings\" from \"the\" north."
print(txt)

# String Methods

# Python has a set of built-in methods that you can use on strings.
# Note: All string methods return new values. They do not change the original string

s= "hello DEAR How are you.ok"
print(s.capitalize())
print (s.count("H"))
print(s.find("z"))
print(s.replace("hello","hi"))
print(s.split())
print(s.upper())
print(s.lower())

s = "-"
seq = ("a", "b", "c")
print(s.join(seq))  # Output: "a-b-c"