# AND (&), OR (|), SHORT CIRCUIT AND (&&), SHORT CIRCUIT OR (||), XOR (^), NOT (!)
import time

# AND/OR - Evaluates both conditions
# SHORT CIRCUIT OR/AND - Evaluates the second condition only when necessary.
# SHORT CIRCUIT AND - Only evaluates the second condition if the first condition is true.
# SHORT CIRCUIT OR - Only evaluate the second condition if the first condition is false.


def delete_even_numbers(input_list: list):
    length_of_list = len(input_list)
    for index in range(length_of_list - 1, -1, -1):
        if input_list[index] % 2 == 0:
            print(f"Deleting {input_list[index]}")
            del input_list[index]
    # return [number for number in input_list if number % 2 != 0]


list1 = [1, 2, 2, 3, 4, 5]
delete_even_numbers(list1)
print(list1)


def heavy_condition() -> bool:
    time.sleep(1)
    print("heavy condition")
    return True


def light_condition() -> bool:
    time.sleep(0.1)
    print("light condition")
    return False


if light_condition() and heavy_condition():
    print("Both conditions have been satisfied.")
else:
    print("Both conditions haven't been satisfied.")

if light_condition() & heavy_condition():
    print("Both conditions have been satisfied.")
else:
    print("Both conditions haven't been satisfied.")

if list1 is not None:
    print("Yay! list1 is not None.")

if list1[0] != 10:
    print("First value in list is not 10.")

if not(list1[0] % 2 == 0):
    print("First number is not even")

if ~(list1[0] % 2 == 0):
    print("First number is not even")

# TODO: Try the short circuit (|) & normal OR operators.

#this "or" evaluates both condition even if the firs is true 
if heavy_condition() | light_condition():
    print("Only one condition is satified")

#this "or" evaluates the second condition only when necessary
if heavy_condition() or light_condition():
    print("Only one condition is satified")

# Exclusive OR - Only one condition has to be true
condition1 = False
condition2 = True
if condition1 ^ condition2:
    # (condition1 and not condition2) or (not condition1 and condition2)
    print("Only one condition is true.")
