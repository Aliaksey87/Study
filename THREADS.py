# responses = []
# for _ in range(5):
#    responses.append(
#        api()
#    )

from datetime import datetime
import threading
import time
import random

# def fn(result, a):
#     print('fn начала исполняться с аргументом: ' + str(a))
#     time.sleep(2)
#     result['result'] = a + 5
#
# def experiment():
#     threads = []
#     for _ in range(3):
#         result = {}
#         t = threading.Thread(target=fn, args=(result, random.randint(1, 100)))    # класс который принимает функ.
#         t.start()
#         threads.append([t, result])
#     thread_number = 1
#     for thread, result in threads:
#         thread.join()
#         print("Поток " + str(thread_number) + ' вернул ' + str(result['result']))
#         thread_number = thread_number + 1
#
# if __name__ == "__main__":
#     experiment()

# 1. Выполнить функцию api последовательно 5 раз и просуммировать возвращаемые числа.
#    Засечь время выполнения всей программы.


def api(result):
    time.sleep(3)
    result['key'] = random.randint(1, 100)


# def fn(result, a):
#     print('fn начала исполняться с аргументом: ' + str(a))
#     time.sleep(2)
#     result['result'] = a + 5

def experiment():
    start = datetime.now()
    x = 0
    for _ in range(5):
        a = {}
        api(a)
        x += a['key']
        print(a['key'])
    execution_time = datetime.now() - start
    print("Время работы: " + str(execution_time.total_seconds()) + ' секунд')
    print('Сумма всех чисел', x)


def experiment2():
    start = datetime.now()
    threads = []
    x = 0
    for _ in range(5):
        result = {}
        t = threading.Thread(target=api, args=(result,))    # класс который принимает функ.
        t.start()
        threads.append([t, result])
    thread_number = 1
    for thread, result in threads:
        thread.join()
        print("Поток " + str(thread_number) + ' вернул ' + str(result['key']))
        x += result['key']
        thread_number = thread_number + 1
    execution_time = datetime.now() - start
    print("Время работы: " + str(execution_time.total_seconds()) + ' секунд')
    print('Сумма всех чисел', x)


if __name__ == "__main__":
    experiment()
