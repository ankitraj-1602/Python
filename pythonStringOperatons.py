# modify string/

a = "  Hello, World!  "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H","h"))
print(a.split(","))
print(a.split(" "))

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format

# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# But we can combine strings and numbers by using f-strings or the format() method!


# F-Strings

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age= 33
txt= f"age is {age}"
print(txt)

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

txt = f"price is {price:.3f} dollars"
print(txt)

txt = f"price is {price*3} dollars"
print(txt)