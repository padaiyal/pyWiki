import time


def time_it_in_milliseconds(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            function(*args, **kwargs)
        except Exception as e:
            print(e)
        return (time.time() - start_time) * 1000
    return wrapper
