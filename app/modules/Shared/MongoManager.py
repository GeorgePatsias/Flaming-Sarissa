from pymongo import MongoClient
from modules.Shared.Logger import logger
from config import MONGO_URI, MONGO_CONNECT


def mongo_connection():
    try:
        return MongoClient(MONGO_URI, connect=MONGO_CONNECT)

    except Exception as e:
        logger.exception(e)
        return None
