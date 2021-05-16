from wiki.utils.time_it import time_it_in_milliseconds

fruits_dict1 = dict()
fruits_dict2 = dict()


@time_it_in_milliseconds
def add_fruit(fruit: str) -> None:
    if fruit not in fruits_dict1:
        fruits_dict1[fruit] = 0
    fruits_dict1[fruit] = fruits_dict1[fruit] + 1


@time_it_in_milliseconds
def add_fruit_with_get(fruit: str) -> None:
    fruits_dict2[fruit] = fruits_dict2.get(fruit, 0) + 1


# Minimal or no performance gain when updating a key that's already present, but significant gain when adding new keys.
if __name__ == '__main__':
    add_fruit_time_average_in_milliseconds = 0
    add_fruit_time_with_get_average_in_milliseconds = 0
    update_fruit_time_average_in_milliseconds = 0
    update_fruit_time_with_get_average_in_milliseconds = 0
    n = 10000
    fruit_to_update = "apple"
    for index in range(n):
        add_fruit_time_average_in_milliseconds += add_fruit(index)
        add_fruit_time_with_get_average_in_milliseconds += add_fruit_with_get(index)
        update_fruit_time_average_in_milliseconds += add_fruit(fruit_to_update)
        update_fruit_time_with_get_average_in_milliseconds += add_fruit_with_get(fruit_to_update)
    add_fruit_time_average_in_milliseconds /= n
    add_fruit_time_with_get_average_in_milliseconds /= n
    update_fruit_time_average_in_milliseconds /= n
    update_fruit_time_with_get_average_in_milliseconds /= n
    print(f"Average time taken to add a new fruit in a regular way: "
          f"{'{0:.6f}'.format(add_fruit_time_average_in_milliseconds)} milliseconds.")
    print(f"Average time taken to update a fruit in a regular way: "
          f"{'{0:.6f}'.format(update_fruit_time_average_in_milliseconds)} milliseconds.")
    print(f"Average time taken to add a new fruit using get(): "
          f"{'{0:.6f}'.format(add_fruit_time_with_get_average_in_milliseconds)} milliseconds.")
    print(f"Average time taken to update a fruit using get(): "
          f"{'{0:.6f}'.format(update_fruit_time_with_get_average_in_milliseconds)} milliseconds.")
