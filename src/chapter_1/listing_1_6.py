import threading

from ..util.time_it import time_it


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print(f'fib({number}) равно {fib(number)}')


@time_it("Время выполнения с потоками:")
def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fib, args=(35,))
    forty_first_thread = threading.Thread(target=print_fib, args=(36,))
    fortieth_thread.start()
    forty_first_thread.start()
    fortieth_thread.join()
    forty_first_thread.join()


def main():
    fibs_with_threads()


if __name__ == "__main__":
    main()
