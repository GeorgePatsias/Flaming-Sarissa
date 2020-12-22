import re
from flask_login import login_user
from modules.Shared.Logger import logger
from modules.Shared.Roles import requires_roles
from flask_login import login_required, current_user, logout_user
from modules.Login.controllers import authorized_login, is_safe_url
from flask import request, render_template, Blueprint, redirect, abort, url_for


app = Blueprint('login', __name__)


@app.route('/login', methods=['GET'])
def login_view(error_message=''):
    try:
        if current_user.is_authenticated:
            return redirect('/', code=302)

        return render_template('login.html', error_message=error_message)

    except Exception as e:
        logger.exception(e)
        return render_template('login.html', error_message='*Invalid Credentials!')


@app.route('/login', methods=['POST'])
def login_verification():
    try:
        auth_user = authorized_login(request.form['email'], request.form['password'])
        if not auth_user:
            return login_view('*Invalid Credentials!')

        login_user(auth_user, remember=False)
        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)

        return redirect(url_for('dashboard.dashboard_view'))

    except Exception as e:
        logger.exception(e)
        return login_view('*Invalid Credentials!')


@app.route('/logout', methods=['GET'])
@login_required
def logout_session():
    try:
        logout_user()
        return redirect('/login', code=302)

    except Exception as e:
        logger.exception(e)
        return redirect('/login', code=302)
