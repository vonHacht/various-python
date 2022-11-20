import logging
from logs import init_output_formatters
import time
from multiprocessing import Process, Queue


class MultiprocessClass:
    __instance = None

    def __new__(cls, *args, **kwargs):

        if not cls.__instance:
            logging.info("first instance, new")

            cls.__instance = object.__new__(cls)

            cls.__instance.__initialized = False
        else:
            logging.info("new")

        return cls.__instance

    def __init__(self, log_level: str = 'normal'):

        if not self.__initialized:
            logging.info("first instance, init")

            self.__queue = Queue(maxsize=1)

            self.__process = Process(target=self.process, args=(log_level, self.__queue))
        else:
            logging.info("init")

        self.__initialized = True

    def process(self, log_level, queue):
        init_output_formatters(log_level)

        cnt = 0
        while 1:
            time.sleep(2)
            logging.info(f'Running process\nQueue size {queue.qsize()}')

            while not queue.empty():
                queue.get()

            queue.put([42 + cnt, None, 'hello'])
            cnt = cnt + 1

    def start(self):
        if not self.__process.is_alive():
            logging.info('Starting process')

            self.__process.start()
        else:
            logging.info('Process already started')

    def stop(self):
        if self.__process.is_alive():
            logging.info('Killing process')

            self.__process.kill()
        else:
            logging.info('Process already killed')

    def get(self):
        value = None

        if not self.__queue.empty():
            value = self.__queue.get()

        return value


if __name__ == '__main__':
    init_output_formatters('debug')

    logging.info("Running")

    mpc = MultiprocessClass('debug')
    MultiprocessClass()
    MultiprocessClass().start()
    time.sleep(20)
    print(mpc.get())
    MultiprocessClass().stop()
