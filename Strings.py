# Strings -> a group of characters
# Strings can be created using single double quotes,double single quotes, triple double quotes and triple single quotes
# It might sound a little confusing but below are examples.
x = "abc"
y = 'abc'
z = """"abc"""
a = '''abc'''

# Substring -> a substring is a string inside a string. In python any character in a string is a string itself
# (substring)

# In the above strings a, ab, bc and abc are all substrings of abc


# Indexing
# Just like in collections, indexing is also possible with strings. We can grab a str using indexing
# IMO Indexing is a really important concept especially with Data Structures as it determines how optimal your code is.
text = "I love python"
print(text[2])

# Slicing -> This is grabbing a range of elements from a str or a collection
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
text3 = text2.upper()  # Converts text to upper case
print(text3)

text4 = text3.lower()  # Converts text to lower case
print(text4)

text5 = text4.capitalize()
print(text5)  # Converts the first letter of the string to a capital letter

text6 = text5.title()
print(text6)  # Converts str to title case

# String Formatting

price = 100
text7 = "The cars' windows cost {} dollars"
text8 = text7.format(price)  # This will replace the curly braces with 100
print(text8)

# Replacing strings
text9 = text5.replace("python", "C++")
print(text9)

# Joining Strings
# first create a set of strings
text10 = ["I", "love", "python"]
text11 = " ".join(text10)  # Joins the elements of the list of str seperated by a white space
print(text11)

# Counting substrings

text12 = "aabbccddeea"

print(text12.count("a"))  # Counts the number of times a substring occurs in a superstring

text13 = "Greetings from earth"
print(text13.find("G"))  # Prints the index of the first occurrence of a substring

bool1 = text13.isupper()  # Returns true or false based on whether the str is uppercase or lowercase
print(bool1)

text14 = ""
bool2 = text14.isspace()  # Checks whether the str is all white space. If it is it returns true and if it's not it
# returns false
print(bool2)

text15 = "12345"
bool3 = text15.isnumeric()  # Returns true if the str contains any number 0-9
print(bool3)

text16 = "I was number 4"
bool4 = text16.isdigit()  # Returns true if the str contains digits only (0-9)
print(bool4)


def hello(name1):
    print("Hello " + name1)


hello("Eddy")
hello("Esther")
