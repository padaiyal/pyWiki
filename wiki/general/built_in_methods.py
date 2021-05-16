from functools import reduce

numbers = range(100, 0, -1)
squared_numbers = map(lambda x: x*x, numbers)
sum_of_squared_numbers = sum(squared_numbers)
product_of_squared_numbers = reduce(lambda x, y: x * y, squared_numbers, 1)


print(squared_numbers)
print(sum_of_squared_numbers)
print(product_of_squared_numbers)
