from threading import Thread
from multiprocessing import Process
import time

N = 500000


def get_fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


if __name__ == '__main__':
    file = open('./artifacts/4_1.txt', 'w')

    start = time.time()
    for _ in range(10):
        fibonacci = get_fibonacci(N)
    delta = round(time.time() - start, 6)
    print(f'sync call finished in {delta} seconds')
    file.write(str(delta) + '\n')

    start = time.time()
    workers = []
    for _ in range(10):
        workers.append(Thread(target=get_fibonacci, args=(N,)))
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    delta = round(time.time() - start, 6)
    print(f'threaded call finished in {delta} seconds')
    file.write(str(delta) + '\n')

    start = time.time()
    workers = []
    for _ in range(10):
        workers.append(Process(target=get_fibonacci, args=(N,)))
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    delta = round(time.time() - start, 6)
    print(f'multiprocessing call finished in {delta} seconds')
    file.write(str(delta) + '\n')

    file.close()
