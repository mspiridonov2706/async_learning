import requests

from src.util.time_it import time_it


def read_example() -> None:
    response = requests.get('https://www.example.com')
    print(response.status_code)


@time_it("Синхронное выполнение заняло")
def main():
    read_example()
    read_example()
