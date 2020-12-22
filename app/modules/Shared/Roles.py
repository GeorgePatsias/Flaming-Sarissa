from functools import wraps
from flask import redirect, url_for
from flask_login import current_user


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role in roles:
                return f(*args, **kwargs)
            return redirect(url_for('login'))

        return wrapped

    return wrapper
