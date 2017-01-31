import hashlib


def encode(password):
    h = hashlib.sha256(password.encode('utf-8'))
    return h.hexdigest()
