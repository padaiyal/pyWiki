import time
from time import process_time, process_time_ns

from wiki.design_patterns.singleton import IsaacEdition


def duration_in_milliseconds_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            function(*args, **kwargs)
        except Exception as e:
            print(e)
        return (time.time() - start_time) * 1000

    return wrapper


# Decorators can also be used as annotations in python.
@duration_in_milliseconds_decorator
def test_method() -> None:
    time.sleep(2)


if __name__ == '__main__':
    isaacEdition = IsaacEdition()
    isaacEdition.set_engine_on(True)
    isaacEdition.set_speed_in_kmph(300)
    decorator_function_benchmark = duration_in_milliseconds_decorator(lambda: None)
    decorator_function = duration_in_milliseconds_decorator(isaacEdition.is_speed_possible)
    print(decorator_function_benchmark())
    print(decorator_function(350))

    # CPU time -
    print(process_time_ns())
    time.sleep(1)
    print(process_time_ns())

    # Epoch time - Number of seconds/milliseconds/nanoseconds or any duration since January 1st 1970.
    print(time.time_ns())
    time.sleep(1)
    print(time.time_ns())

    print(1_600_000_000/(86_400 * 365))

    print(test_method())

# TODO: Implement a decorator that returns the CPU time taken by the function.
