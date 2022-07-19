# Sets  -> an unordered collection of elements without duplicate
collection = {"a", "b", "c", "d"}

collection.add("f")

print(collection)

collection.clear()
print(len(collection))

# To remove an element from a set

coll2 = {"2", "3", "4"}

coll2.discard("2")
print(coll2)

# To remove a random element from the set use pop

coll2.pop()
print(coll2)

# To see the difference between two sets use the difference function
a = {"1", "2", "3"}
b = {"3", "4", "5"}

c = a.difference(b)
print(c)

# To create an intersection set or print out common elements use the intersection function
d = a.intersection(b)
print(d)

# To combine two or more sets use the combine function

e = a.union(b)
print(e)

# To check whether a set is a subset/superset of another set, use isset and issubset functions respectively

f = {"a", "b", "c"}
g = {"a", "b"}

h = g.issubset(f)  # Boolean True because g is a subset of f
print(h)

i = f.issuperset(g)  # Boolean True because f is a superset of g
print(i)
