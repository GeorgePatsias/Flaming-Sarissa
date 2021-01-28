from modules.Shared.Logger import logger
from modules.Login.controllers import is_safe_url
from flask_login import login_required, current_user
from flask import request, render_template, Blueprint, redirect
from modules.Profile.controllers import edit_profile, get_profile, update_profile


app = Blueprint('profile', __name__)


@app.route('/profile', methods=['GET'])
@login_required
def profile_view():
    try:
        return render_template('profile.html', profile_data=get_profile(current_user.get_id()))

    except Exception as e:
        logger.exception(e)
        return render_template('profile.html', profile_data={})


@app.route('/profile', methods=['POST'])
@login_required
def profile_form():
    try:
        if not edit_profile(current_user.get_id(), request.form):
            return '', 400

        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)

        return redirect('/profile', code=302)

    except Exception as e:
        logger.exception(e)
        return '', 500


@app.route('/profile-connections', methods=['POST'])
@login_required
def profile_connections():
    try:
        if not update_profile(current_user.get_id(), request.form):
            return '', 400

        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)

        return redirect('/profile', code=302)

    except Exception as e:
        logger.exception(e)
        return '', 500
