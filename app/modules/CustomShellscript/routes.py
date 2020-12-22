from modules.Shared.Logger import logger
from flask_login import login_required, current_user, logout_user
from flask import request, render_template, Blueprint, redirect, abort, url_for


app = Blueprint('custom_shellscript', __name__)


@app.route('/custom_shellscript', methods=['GET'])
@login_required
def custom_shellscript_view():
    try:
        return render_template('custom_shellscript.html')

    except Exception as e:
        logger.exception(e)
        return render_template('custom_shellscript.html')
