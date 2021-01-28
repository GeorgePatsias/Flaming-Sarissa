from os import urandom, path
from modules.Shared.User import User
from datetime import timedelta, datetime
from modules.Shared.Logger import logger
from modules.Shared.MongoManager import mongo_connection
from flask import Flask, session, render_template, send_from_directory
from config import MONGO_DB, MONGO_USERS_COLL, SESSION_EXPIRE
from flask_login import login_required, current_user, LoginManager, login_user, UserMixin

import modules.Nmap.routes
import modules.Login.routes
import modules.Profile.routes
import modules.Dashboard.routes
import modules.UserManagement.routes
import modules.CustomShellscript.routes

app = Flask(__name__)
app.config.from_pyfile('config.py')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'
login_manager.refresh_view = 'login'
login_manager.needs_refresh_message = (u"Session time out, please re-login")
login_manager.needs_refresh_message_category = "info"

app.register_blueprint(modules.Nmap.routes.app)
app.register_blueprint(modules.Login.routes.app)
app.register_blueprint(modules.Profile.routes.app)
app.register_blueprint(modules.Dashboard.routes.app)
app.register_blueprint(modules.UserManagement.routes.app)
app.register_blueprint(modules.CustomShellscript.routes.app)


@login_manager.user_loader
def load_user(email):
    try:
        users_collec = mongo_connection()[MONGO_DB][MONGO_USERS_COLL]
        data = users_collec.find_one({'email': email})
        if not data:
            mongo_connection().close()
            return

        user = User()
        user.id = email
        users_collec.update_one({'email': email},
                                {'$set': {'last_activity': str(datetime.now().strftime("%Y-%m-%d %H:%M"))}})
        mongo_connection().close()

        return user

    except Exception as e:
        logger.exception(e)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static/img/'), 'favicon.ico')


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=SESSION_EXPIRE)
    session.modified = True


if __name__ == '__main__':
    app.secret_key = urandom(60)
    app.run(
        host=app.config['FLASK_HOST'],
        port=app.config['FLAST_PORT'],
        debug=app.config['FLASK_DEBUG'],
        threaded=app.config['FLASK_THREADED']
    )
