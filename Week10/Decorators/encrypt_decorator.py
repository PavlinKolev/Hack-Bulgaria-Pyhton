def caesar_cipher(key, string):
    result = ""
    for ch in string:
        result += chr(ord(ch) + key)
    return result


def encrypt(key):
    def accepter(func):
        def encrypt_function():
            string = func()
            if type(string) is not str:
                raise TypeError("Return type of decorated function must be string.")
            return caesar_cipher(key, string)
        return encrypt_function
    return accepter
