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
# Python gives us access to strength functions when working with strings such as endswith() and startswith

# StartsWith() -> Checks whether the string starts with a specific substring
name = "Python"
if name.startswith("P"):
    print("Name starts with P")
# Endswith() -> Checks whether the string ends with a specific substring
if name.endswith("n"):
    print("Name ends with n")

# Python allows us to convert strings to uppercase and lower case.
text2 = "i love python"

