from modules.Shared.Logger import logger
from modules.Login.controllers import is_safe_url
from flask_login import login_required, current_user
from modules.UserManagement.controllers import get_users, add_user, delete_user
from flask import request, render_template, Blueprint, jsonify, redirect, url_for


app = Blueprint('user_management', __name__)


@app.route('/user-management', methods=['GET'])
@login_required
def user_management():
    try:
        return render_template('user_management.html')

    except Exception as e:
        logger.exception(e)
        return render_template('user_management.html')


@app.route('/user-management/get/users', methods=['GET'])
@login_required
def datatable_data():
    try:
        return jsonify({'data': get_users()}), 200

    except Exception as e:
        logger.exception(e)
        return {'data': {}}, 500


@app.route('/user-management/add/user', methods=['POST'])
@login_required
def create_user():
    try:
        if not add_user(request.form):
            return '', 400

        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)

        return redirect('/user-management', code=302)

    except Exception as e:
        logger.exception(e)
        return '', 500


@app.route('/user-management/delete/user', methods=['POST'])
@login_required
def remove_user():
    try:
        if not delete_user(request.get_json()):
            return '', 400

        return '', 200

    except Exception as e:
        logger.exception(e)
        return '', 500
