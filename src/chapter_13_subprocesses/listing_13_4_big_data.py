"""Порождение большого объема вывода"""

import sys


[sys.stdout.buffer.write(b"Hello!!\n") for _ in range(1000000)]

sys.stdout.flush()
