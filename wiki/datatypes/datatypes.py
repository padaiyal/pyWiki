import math

# Type hinting is optional, but recommended as it improves code readability and checking for type mismatches later.
number: int = 100
decimal: float = 3.141569
string: str = "Isaac"
complex_number: complex = complex(1, 2)
boolean: bool = True

# Type casting
number2: int = int(decimal)# Default behaviour is equivalent to that of floor().
ceilNumber: int = math.ceil(decimal)
floorNumber: int = math.floor(decimal)
print(number2)
print(ceilNumber)
print(floorNumber)

# Python has type hinting, NOT type enforcement. For the below example, it doesn't enforce the hinted type.
number3: float = int(decimal)

"""
Collections

For each collection:
 - Create empty collection
 - Modify collection
 - Check for existence of an element in the collection
 - Try to mimic the pass by reference example
 - Create a copy
 - Merge the collections
 - Iterate through the collection
"""

# list

# Empty list
lst0: list = list()

lst1: list = [1, 2, 3]
print(len(lst1))
print(lst1)
lst1.append(4)
print(lst1)

# Merge two lists.
lst2 = [7, 8, 9]
lst3: list = lst1 + lst2
print(lst3)

# CAUTION: Collections are passed by reference!!
lst4: list = lst3
lst4[0] = 10
print(f"lst3: {lst3}")
print(f"lst4: {lst4}")

lst4: list = list(lst3)
lst4[0] = 11
print(f"lst3: {lst3}")
print(f"lst4: {lst4}")

# Delete an element
del lst3[0]
print(lst3)

if 10 in lst3:
    print("10 is present in lst3!")
else:
    print("10 is not present in lst3!")

# Iterating through the list.
for element in lst3:
    print(element)

for index in range(len(lst3)):
    print(lst3[index])

for index, element in enumerate(lst3):
    # print(index + ":" + element)
    print(f"{index}:{element}")

print(enumerate(lst3))


# Dictionary
dict0: dict = dict()

# The keys in a dictionary have to be unique, but not the values.
dict1: dict = {
    "key1": 1,
    "key2": 2,
}
print(dict1)

# Update the value for an existing key.
dict1["key1"] = 11
print(dict1)

# Add a new key-value pair.
dict1["key3"] = 3
print(dict1)

# Delete a key-value pair
del dict1["key1"]
print(dict1)

# Check for existence of a key.
if "key1" in dict1:
    print("key1 found in dictionary!")
else:
    print("key1 not found in dictionary!")

# Check for existence of a value.
if 2 in dict1.values():
    print("Value 2 found in dictionary!")
else:
    print("Value 2 not found in dictionary!")

# BEWARE pass by reference!
dict2: dict = dict1
dict2["key10"] = 10
print(dict1)
print(dict2)

dict3: dict = dict(dict1)
dict3["key11"] = 11
print(dict1)
print(dict3)

# Merging two dictionaries
dict4: dict = {
    "key10": 1010101010,
    "key11": 11,
    "key12": 12
}
dict5: dict = dict(dict1)
dict5.update(dict4)
print(dict1)
print(dict5)

# Iterating through dictionaries
for element in dict5:
    print(element)

for key, value in dict5.items():
    print(f"{key}: f{value}")


# Setting/Getting default value if it doesn't exist.
if "key99" not in dict5:
    dict5["key99"] = 99

dict5["key99"] = dict5.get("key99", default=99)

# TODO: set, tuple, frozenset
