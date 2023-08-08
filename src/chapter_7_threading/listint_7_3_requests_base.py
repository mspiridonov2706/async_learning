"""Базовое использование requests"""

import requests


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


def main():
    url = 'https://www.example.com'
    print(get_status_code(url))
    print(get_status_code(url))


if __name__ == "__main__":
    main()
