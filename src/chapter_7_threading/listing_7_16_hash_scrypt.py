"""Хеширование паролей с помощью алгоритма scrypt"""

import hashlib
import os
import string
import time
import random


def random_password(length: int) -> bytes:
    ascii_lowercase = string.ascii_lowercase.encode()
    return b''.join(bytes(random.choice(ascii_lowercase)) for _ in range(length))


def hash(password: bytes) -> str:
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))


def main():
    passwords = [random_password(10) for _ in range(10000)]
    start = time.time()
    for password in passwords:
        hash(password)
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()
