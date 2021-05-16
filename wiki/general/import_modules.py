from wiki.utils.time_it import time_it_in_milliseconds


@time_it_in_milliseconds
def standard_check():
    pass


@time_it_in_milliseconds
def import_check():
    import numpy
    import urllib3


if __name__ == '__main__':
    print(f"Check for a standard function call: {import_check()} ms")
    print(f"Check for a standard function call: {import_check()} ms")
