from time import process_time
from math import sqrt
from functools import wraps


def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = process_time()
        result = func(*args, **kwargs)
        elapsed_time = process_time() - t

        print(f'Execution time: {elapsed_time}')
        return result

    return wrapper


@measure_execution_time
def my_func(x):
    return [sqrt(x) for x in range(x)]


my_func(10000000)