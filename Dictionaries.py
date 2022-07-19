# Dictionary -> an unordered collection of key-value pairs.
# Dictionaries rely on the concept of hashing whereby instead of having elements being ordered by indexes they are
# ordered by a unique key. This key has to be unique and immutable.

# 1st way of creating dict
collection = dict()
collection["key1"] = "value1"
collection["key2"] = "value2"
collection["key3"] = "value3"

# 2nd way of creating dict

collection2 = {}  # This is an empty dictionary.

collection3 = {"key1": "value1", "key2": "value2", "key3": "value3"}

# To clear items from a dictionary we use the clear function below
collection3.clear()

# To retrieve a value from a dictionary we use the key string and a get function
print(collection.get("key1"))

value1 = collection.get("key1")
print(value1)

# To remove an item from a dictionary, use the POP function

collection.pop("key1")
print(collection)

# Iteration in dictionaries -> using the for loop it is possible to loop through both values and keys

for i in collection.keys():  # -> This will print the keys only
    print(i)

for i in collection.values():   # ->This will loop through the values only
    print(i)
    
