# List -> This is an ordered collection of Data

list1 = [1, 2, 3, 4, 5, 7, 8, 9]  # This is a list of integers

# Checking the length of a list
print(len(list1))

# Indexing -> Indexing starts at 0
list1[0] = 6
print(list1[:])  # This will print every value of the list in the order they appear

print(list1[0:5])  # This will print the list of values from index 0 to 4

print(list1[0:-1])  # This will print the list of values from 0 to 7 (the last index minus 1)

# Iteration (for loop)

for i in range(len(list1)):
    print(list1[i])  # This will print out the whole collection

    # Checking if a value is in the list
if 1 in list1:
    print("1 is in list")
else:
    print("1 is not in the list")

# Append Function -> Used to add elements at the end of the list

list1.append(10)  # 10 Was added to the end of the list
print(list1[:])

# Clear Function -> Used to clear all the items in the list

list1.clear()
print(list1[:])  # Prints an empty list

# Sorting -> Used to sort a list
integers = [4, 3, 8, 2, 1, 5]
integers.sort()  # -> Sorts in ascending order
print(integers[:])

# Sort Reversing -> Reversing between ascending and descending order
integers.reverse()  # -> Sorts in reversing order (ascending/descending)
print(integers[:])

# Count function -> used to count how man times an element appears in a list
print(integers.count(3))  # -> prints out 1 because 3 appears in the list only once

# Extend Function -> Used to combine two lists
staff = [1, 2, 3]
managers = [4, 5, 6]
staff.extend(managers)
print(staff)

# Index Function -> Used to find out the index of an element in a list
students = [2, 8, 5, 6, 9]
print(students.index(5))

# Insert Function -> Used to insert an element in a list using an index
students.insert(3, 18)
print(students[3])
print(students)

# Removing values from a list

# 1. Using the pop function -> The pop function removes items based on their indexes
students.pop(2)
print(students)

# 2. Using the remove function -> Removes items from a list based on their values.
students.remove(18)
print(students)