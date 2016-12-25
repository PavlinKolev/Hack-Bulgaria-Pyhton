import time
from functools import wraps


def performance(file_name):
    def accepter(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            with open(file_name, 'a') as f:
                f.write("{} was called and took ".format(func.__name__) +
                "{:.2f} seconds to complete\n".format(end_time - start_time))
            return result
        return decorator
    return accepter
