"""Использование объекта CustomFuture в цикле"""

from src.chapter_14_advanced_asyncio.listing_14_8_custom_future import CustomFuture


def main():
    future = CustomFuture()
    i = 0

    while True:
        try:
            print("Проверяется будущий объект...")
            gen = future.__await__()
            gen.send(None)
            print("Будущий объект не готов...")
            if i == 2:
                print("Устанавливается значение будущего объекта...")
                future.set_result("Готово!")
            i = i + 1
        except StopIteration as si:
            print(f"Значение равно: {si.value}")
            break
