"""Приложение echo"""

from random import randrange
import time


user_input = ""
while user_input != "quit":
    user_input = input("Input text: ")
    for i in range(randrange(10)):
        time.sleep(0.5)
    print(user_input)
