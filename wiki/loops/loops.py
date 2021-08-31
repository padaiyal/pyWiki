# for loop
for index in range(1, 10, 2):
    print(index)

index = 10
while index >= 0:
    print(index)
    index -= 1

lst1 = [1, 1, 2, 3]
lst2 = list()
for element in lst1:
    lst2.append(element * element)
print(lst1)
print(lst2)

# list comprehension/generators
lst3 = list(element * element for element in lst1)
set1 = set(element * element for element in lst1)
dict1 = {element: element * element for element in lst1}

even_number_squares = [element * element for element in lst1 if element % 2 == 0]
tuple1 = tuple(element * element for element in lst1)

result = (2 * 3)/4
print(lst3)
print(set1)
print(dict1)
print(even_number_squares)
print(tuple1)
