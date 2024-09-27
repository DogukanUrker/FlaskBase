from hashlib import sha3_512
from secrets import token_bytes

from time import time


def generateID(inputString):
    byteInput = inputString.encode()

    timestamp = str(time()).encode()

    randomBytes1 = token_bytes(64)
    randomBytes2 = token_bytes(32)
    randomBytes3 = token_bytes(16)

    hasher = sha3_512()

    hasher.update(byteInput)
    hasher.update(timestamp)
    hasher.update(randomBytes1)
    hasher.update(randomBytes2)
    hasher.update(randomBytes3)

    return hasher.hexdigest()
