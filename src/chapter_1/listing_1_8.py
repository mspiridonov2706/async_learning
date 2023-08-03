import threading
import requests

from src.util.time_it import time_it


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


@time_it("Многопоточное выполнение заняло")
def main():
    thread_1 = threading.Thread(target=read_example)
    thread_2 = threading.Thread(target=read_example)

    thread_1.start()
    thread_2.start()
    print('Все потоки работают!')

    thread_1.join()
    thread_2.join()
