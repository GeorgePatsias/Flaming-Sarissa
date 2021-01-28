from flask import escape
from modules.Shared.Logger import logger
from config import MONGO_DB, MONGO_USERS_COLL
from modules.Shared.MongoManager import mongo_connection
from werkzeug.security import generate_password_hash, check_password_hash

mongo_client = mongo_connection()
db = mongo_client[MONGO_DB]
users_collec = db[MONGO_USERS_COLL]


def get_profile(user_id):
    try:
        return users_collec.find_one({'email': user_id}, {'_id': 0, 'password': 0})

    except Exception as e:
        logger.exception(e)
        return None

def get_DO_token(user_id):
    try:
        user = users_collec.find_one({'email': user_id}, {'_id': 0, 'do_token': 1})
        return user.get('do_token', '')

    except Exception as e:
        logger.exception(e)
        return None
    

def edit_profile(user_id, data):
    try:
        current_password = data['current_password']
        new_password = data['new_password']

        if not current_password or not new_password:
            return False

        user_profile = users_collec.find_one({'email': user_id})

        if not check_password_hash(user_profile['password'], current_password):
            return False

        users_collec.update_one({'email': user_id}, {'$set': {'password': generate_password_hash(new_password)}})

        return True

    except Exception as e:
        logger.exception(e)
        return False


def update_profile(user_id, data):
    try:
        if not data:
            return False

        data = data.to_dict()

        for key, value in data.items():
            if key not in ['do_token', 'ssh_key']:
                continue

            data[key] = value.strip()

        users_collec.update_one({'email': user_id}, {'$set': data})

        return True

    except Exception as e:
        logger.exception(e)
        return False
