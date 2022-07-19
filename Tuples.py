# Tuples -> An unchangeable ordered list
# Tuples apply to same rules as lists, but they cannot be changed and use round brackets instead of square ones

collection = (1, 2, 3)
print(collection[0])

# Tuples are unchangeable/ immutable but there is a way to insert or change values by converting a tuple to a list then
#   convert it back to a tuple

collection2 = list(collection)
collection2[0] = 5
new_collection = tuple(collection2)
print(new_collection[0])
print(new_collection)

for i in new_collection:
    print(i)

students = (1, 2, 3)
staff = (4, 5, 6)
employees = students + staff
print(employees)

students2 = list(students)
staff2 = list(staff)

students2.extend(staff2)

print(students2)

students3 = tuple(students2)
print(students3)

x = students3.count(2)
print(x)
