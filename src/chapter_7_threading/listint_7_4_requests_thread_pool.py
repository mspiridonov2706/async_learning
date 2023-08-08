"""Выполнение запросов с помощью пула потоков"""

import time
import requests
from concurrent.futures import ThreadPoolExecutor


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


def main():
    start = time.time()
    with ThreadPoolExecutor() as pool:
        urls = ['https://www.example.com' for _ in range(1000)]
        results = pool.map(get_status_code, urls)
        for result in results:
            print(result)
        end = time.time()
        print(f'Выполнение запросов завершено за {end - start:.4f} с')


if __name__ == "__main__":
    main()
