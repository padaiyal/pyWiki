from functools import reduce


# map() - Applies the specified function to every element in the collection.
def square(number: int) -> int:
    return number * number


list1 = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, list1))  # [result for result in map(square, list1)]
print(squared_numbers)


# filter() - Filters the elements in the collection that match the predicate/condition.
def is_even(number: int) -> bool:
    return number % 2 == 0


list2 = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, list2))
print(even_numbers)


# reduce() - Reduces a collection of elements into a single value.
def sum(number1: int, number2: int) -> int:
    return number1 + number2


list2 = [1, 2, 3, 4, 5]
sum_of_values = reduce(sum, list2)
print(sum_of_values)
