from twofish import Twofish

def encrypt(key, data):
    T = Twofish(key)
    return T.encrypt(data)

def decrypt(key, data):
    T = Twofish(key)
    return T.decrypt(data)