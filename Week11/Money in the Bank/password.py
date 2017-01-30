import hashlib


def encode(password):
    h = hashlib.sha256(password)
    return h.hexdigest()
