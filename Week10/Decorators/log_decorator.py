import datetime


def log(file_name):
    def accepter(func):
        def execute_func(*args):
            with open(file_name, 'a') as f:
                f.write("{} was called at {}\n".format(
                                                    func.__name__,
                                                    datetime.datetime.now()))
            return func(*args)
        return execute_func
    return accepter
