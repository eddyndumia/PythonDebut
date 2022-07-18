# Boolean
bool1 = True
bool2 = False

print(bool(bool1))

# Any integer positive or negative is Boolean True by nature

x = 3
print(bool(x))  # This is True

# Zero is boolean False

y = 0
print(bool(y))  # This is False

# Any empty collection or list is boolean false and any list or collection with an argument/object is true

r = []  # This is an empty list and is false

print(bool(r))

t = ["1", "2", "3", "4"]  # This is true because it is not empty

print(bool(t))
