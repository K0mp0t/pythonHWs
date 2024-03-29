import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from os import cpu_count
import logging
import time

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(message)s')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

task_logger = logging.FileHandler('artifacts/4_2_tasks.log', mode='w')
task_logger.setLevel(logging.DEBUG)
task_logger.setFormatter(formatter)

time_logger = logging.FileHandler('artifacts/4_2_time.log', mode='w')
time_logger.setLevel(logging.INFO)
time_logger.setFormatter(formatter)

logger.addHandler(task_logger)
logger.addHandler(time_logger)


def worker(i, a, step, n_iter, f):
    logging.debug(f"Worker {i} started")
    acc = sum(f(a + j * step) * step for j in range(i, n_iter, n_jobs))
    return acc


def integrate_parallel(f, a, b, *, n_jobs=1, n_iter=10000000, executor_cls):
    step = (b - a) / n_iter
    with executor_cls(max_workers=n_jobs) as executor:
        futures = {executor.submit(worker, i, a, step, n_iter, f): i for i in range(n_jobs)}
        acc = sum(future.result() for future in as_completed(futures))
    return acc


# так получается медленно. Возможно из-за большого количества тасок, в варианте выше (к которому я шел полтора часа!)
# число тасок равно числу воркеров
def integrate(f, a, b, *, n_jobs=1, n_iter=10000, executor_cls=None):
    step = (b - a) / n_iter
    with executor_cls(max_workers=n_jobs) as executor:
        futures = [executor.submit(f, a + i * step) for i in range(n_iter)]
        acc = sum(future.result() for future in as_completed(futures)) * step
    return acc


# здесь вообще интересный результат. У меня 6 физических ядер с hyper threading'ом.
# Наиболее оптимальное количество тасок - около 6 (внезапно).
# Около 6 т.к. у меня в фоне есть еще процессы (IDE, браузер)
if __name__ == '__main__':
    for n_jobs in range(1, cpu_count()*2):
        start = time.time()
        integrate_parallel(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_cls=ThreadPoolExecutor)
        logger.info(f'calculated with {n_jobs} jobs and ThreadPoolExecutor in {round(time.time() - start, 6)} seconds')

    for n_jobs in range(1, cpu_count()*2):
        start = time.time()
        integrate_parallel(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_cls=ProcessPoolExecutor)
        logger.info(f'calculated with {n_jobs} jobs and ProcessPoolExecutor in {round(time.time() - start, 6)} seconds')

