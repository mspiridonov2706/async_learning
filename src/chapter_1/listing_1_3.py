import os
import threading


def hello_from_thread():
    print(f"Привет от потока {threading.current_thread().name}!")


def main():
    print(f"Исполняется Python-процесс с идентификатором: {os.getpid()}")
    hello_thread = threading.Thread(target=hello_from_thread)
    hello_thread.start()
    total_threads = threading.active_count()
    thread_name = threading.current_thread().name
    print(f"В данный момент Python выполняет {total_threads} поток(ов)")
    print(f"Имя текущего потока {thread_name}")
    hello_thread.join()


if __name__ == "__main__":
    main()
