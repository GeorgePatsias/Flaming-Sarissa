import json

import requests
from flask import render_template, jsonify, Blueprint
from flask_login import login_required, current_user, logout_user


app = Blueprint('dashboard', __name__)


@app.route('/')
@login_required
def dashboard_view():
    print(current_user.id)
    return render_template('dashboard.html')
