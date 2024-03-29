import io
import time
import logging
from datetime import datetime

LOGGER_NAME = 'root'
LOGGER_DATEFMT = '%Y-%m-%d %H:%M:%S'

handler = logging.StreamHandler()

logger = logging.getLogger(LOGGER_NAME)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def add_logging(logs_path, prefix):
    log_name = prefix + datetime.strftime(datetime.today(), '%Y-%m-%d_%H-%M-%S') + '.log'
    stdout_log_path = logs_path / log_name

    fh = logging.FileHandler(str(stdout_log_path))
    formatter = logging.Formatter(fmt='(%(levelname)s) %(asctime)s: %(message)s',
                                  datefmt=LOGGER_DATEFMT)
    fh.setFormatter(formatter)
    logger.addHandler(fh)


class TqdmToLogger(io.StringIO):
    logger = None
    level = None
    buf = ''

    def __init__(self, logger, level=None, mininterval=5):
        super(TqdmToLogger, self).__init__()
        self.logger = logger
        self.level = level or logging.INFO
        self.mininterval = mininterval
        self.last_time = 0

    def write(self, buf):
        self.buf = buf.strip('\r\n\t ')
 
    def flush(self):
        if len(self.buf) > 0 and time.time() - self.last_time > self.mininterval:
            self.logger.log(self.level, self.buf)
            self.last_time = time.time()
