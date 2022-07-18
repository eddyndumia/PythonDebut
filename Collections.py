# Collections
# They store multiple values. They are like variables but can hold many individual values
# There are 4 main collection types:
#                  1. Lists
#                  2. Dictionaries
#                  3. Tuples
#                  4. Sets


# Lists -> This is an ordered collection of Data

list1 = [1, 2, 3, 4, 5, 7, 8, 9]  # This is a list of integers

# Indexing -> Indexing starts at 0
list1[0] = 6
print(list1[:])  # This will print every value of the list in the order they appear

print(list1[0:5])  # This will print the list of values from index 0 to 4

print(list1[0:-1])  # This will print the list of values from 0 to 7 (the last index minus 1)

# Tuple -> This is an ordered unchangeable collection of data

# Dictionary -> A collection of key-value pairs

# Sets -> An unordered collection of data that does not contain any duplicate
