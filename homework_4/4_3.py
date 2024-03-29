import multiprocessing as mp
import threading
import logging
import time
import codecs

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s - %(message)s')

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

file_handler = logging.FileHandler('artifacts/4_3.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def process_A_worker(input_conn, output_conn):
    def send():
        while True:
            if not queue.empty():
                output_conn.send(queue.get_nowait())
                time.sleep(5)
            time.sleep(0.1)

    def acquire():
        while True:
            if input_conn.poll():
                value = input_conn.recv().lower()
                queue.put(value)
            time.sleep(0.1)

    queue = mp.Queue()

    sender = threading.Thread(target=send)
    acquirer = threading.Thread(target=acquire)

    sender.start()
    acquirer.start()


def process_B_worker(input_conn, output_conn):
    def acquire_and_send():
        while True:
            if input_conn.poll():
                output_conn.send(codecs.encode(input_conn.recv(), 'rot-13'))
            time.sleep(0.1)

    sender = threading.Thread(target=acquire_and_send)
    sender.start()


def main_worker(input_conn, output_conn):
    def send():
        while True:
            inp = input()
            output_conn.send(inp)
            logger.info(f'Sent: {inp}')

    def acquire():
        while True:
            if input_conn.poll():
                logger.info(f'Got: {input_conn.recv()}')
            time.sleep(0.1)

    sender = threading.Thread(target=send)
    acquirer = threading.Thread(target=acquire)

    sender.start()
    acquirer.start()


conn_mA, conn_Ma = mp.Pipe()
conn_aB, conn_Ab = mp.Pipe()
conn_bM, conn_Bm = mp.Pipe()

process_A = mp.Process(target=process_A_worker, args=(conn_mA, conn_Ab))
process_B = mp.Process(target=process_B_worker, args=(conn_aB, conn_Bm))

process_A.start()
process_B.start()

main_worker(conn_bM, conn_Ma)
