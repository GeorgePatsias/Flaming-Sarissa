from sys import stdout
from logging.handlers import RotatingFileHandler
from logging import  StreamHandler, INFO, getLogger
from config import LOGGER_PATH, LOGGER_MAX_BYTES, LOGGER_BACKUP_COUNT

logger = getLogger(name='logstash')
logger.setLevel(INFO)

handler = RotatingFileHandler(LOGGER_PATH, maxBytes=LOGGER_MAX_BYTES, backupCount=LOGGER_BACKUP_COUNT)
stream_handler = StreamHandler(stdout)


logger.addHandler(handler)
logger.addHandler(stream_handler)
