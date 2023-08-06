"""Захват и освобождение блокировки"""

from multiprocessing import Process, Value


def increment_value(shared_int: Value):
    shared_int.get_lock().acquire()
    shared_int.value = shared_int.value + 1
    shared_int.get_lock().release()

    # OR

    # with shared_int.get_lock():
    #     shared_int.value = shared_int.value + 1


def main():
    for _ in range(100):
        integer = Value('i', 0)
        procs = [
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
        ]
        [p.start() for p in procs]
        [p.join() for p in procs]
        print(integer.value)
        assert (integer.value == 2)


if __name__ == "__main__":
    main()
