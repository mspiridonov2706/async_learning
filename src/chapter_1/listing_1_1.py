import requests


def main():
    response = requests.get('https://www.example.com')  # Веб-запрос ограничен производительностью ввода-вывода

    items = response.headers.items()
    headers = [f'{key}: {header}' for key, header in items]  # Обработка ответа ограничена быстродействием процессора

    formatted_headers = '\n'.join(headers)  # Конкатенация строк ограничена быстродействием процессора

    with open('headers.txt', 'w') as file:
        file.write(formatted_headers)  # Запись на диск ограничена производительностью ввода-вывод


if __name__ == "__main__":
    main()
