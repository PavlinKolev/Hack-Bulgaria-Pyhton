from functools import wraps


def caesar_cipher(key, string):
    result = ""
    for ch in string:
        if ch.isalpha():
            result += chr(ord(ch) + key)
        else:
            result += ch
    return result


def encrypt(key):
    def accepter(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            string = func(*args, **kwargs)
            if type(string) is not str:
                raise TypeError("Return type of decorated function must be string.")
            return caesar_cipher(key, string)
        return decorator
    return accepter
