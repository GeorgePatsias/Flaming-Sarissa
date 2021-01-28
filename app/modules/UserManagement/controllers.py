from flask import escape
from datetime import datetime
from modules.Shared.Logger import logger
from config import MONGO_DB, MONGO_USERS_COLL
from modules.Profile.controllers import get_profile
from modules.Shared.MongoManager import mongo_connection
from werkzeug.security import generate_password_hash, check_password_hash

mongo_client = mongo_connection()
db = mongo_client[MONGO_DB]
users_collec = db[MONGO_USERS_COLL]


def get_users():
    try:
        return list(users_collec.find({}, {'_id': 0, 'email': 1, 'last_activity': 1, 'createdAt': '1'}))

    except Exception as e:
        logger.exception(e)
        return {}


def add_user(data):
    try:
        if not data:
            return False

        data = data.to_dict()

        for key, value in data.items():
            if key not in ['email', 'password', 'confirm_password']:
                return False

            data[key] = value.strip()

        if get_profile(data['email']):
            return False

        if data['password'] != data['confirm_password']:
            return False

        data.pop('confirm_password')
        data['createdAt'] = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
        data['last_activity'] = ''
        data['ssh_key'] = ''
        data['do_token'] = ''
        data['password'] = generate_password_hash(data['password'])

        users_collec.insert_one(data)

        return True

    except Exception as e:
        logger.exception(e)
        return False


def delete_user(data):
    try:
        if not data:
            return False

        if 'email' not in data.keys():
            return False

        users_collec.delete_one({'email': data['email']})

        return True

    except Exception as e:
        logger.exception(e)
        return False
