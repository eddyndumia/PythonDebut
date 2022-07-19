# Strings -> a group of characters
# Strings can be created using single double quotes, double single quotes and triple double quotes

x = "abc"
y = 'abc'
z = """"abc"""
a = '''abc'''

# Substring -> a substring is a string inside a string. In python any character in a string is a string itself
# (substring)

# In the above strings a, ab, bc and abc are all substrings of abc


# Indexing
# Just like in collections, indexing is also possible with strings
text = "I love python"
print(text[2])

# Slicing -> This is grabbing a range of elements from a string or a collection
text2 = text[0:7]
print(text2)

# String Functions
# Python gives us access to strength functions when working with strings that are very useful for text formatting.

# StartsWith() -> Checks whether the string starts with a specific substring
name = "Python"
if name.startswith("P"):
    print("Name starts with P")
# Endswith() -> Checks whether the string ends with a specific substring
if name.endswith("n"):
    print("Name ends with n")

text2 = "i love python"
text3 = text2.upper()   # Converts text to upper case
print(text3)

text4 = text3.lower()   # Converts text to lower case
print(text4)

text5 = text4.capitalize()
print(text5)    # Converts the first letter of the string to a capital letter

text6 = text5.title()
print(text6)    # Converts str to title case

# String Formatting

price = 100
text7 = "The cars' windows cost {} dollars"
text8 = text7.format(price)    # This will replace the curly braces with 100
print(text8)


