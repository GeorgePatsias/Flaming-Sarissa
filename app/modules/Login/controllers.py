from uuid import uuid4
from flask import escape, request
from modules.Shared.User import User
from config import USERNAME, PASSWORD
from modules.Shared.Logger import logger
from urllib.parse import urlparse, urljoin
from config import MONGO_DB, MONGO_USERS_COLL
from werkzeug.security import check_password_hash
from modules.Shared.MongoManager import mongo_connection

mongo_client = mongo_connection()
db = mongo_client[MONGO_DB]
users_collec = db[MONGO_USERS_COLL]


def authorized_login(email, password):
    try:
        if not email or not password:
            return None

        email = escape(email).strip().lower()

        authorized_user = users_collec.find_one({'email': email}, {'_id': 0})

        if not authorized_user:
            return None

        if not check_password_hash(authorized_user.get('password', ''), password):
            return None

        user = User()
        user.id = email
        user.token = str(uuid4())

        return user

    except Exception as e:
        logger.exception(e)
        return None


def is_safe_url(target):
    try:
        ref_url = urlparse(request.host_url)
        test_url = urlparse(urljoin(request.host_url, target))
        return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

    except Exception as e:
        logger.exception(e)
