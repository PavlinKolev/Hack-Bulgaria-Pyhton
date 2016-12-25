import datetime
from functools import wraps

def log(file_name):
    def accepter(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            with open(file_name, 'a') as f:
                f.write("{} was called at {}\n".format(
                                                    func.__name__,
                                                    datetime.datetime.now()))
            return func(*args, *kwargs)
        return decorator
    return accepter
