from flask_login import login_required
from modules.Shared.Logger import logger
from modules.Nmap.controllers import retrieve_specs
from flask import request, render_template, Blueprint



app = Blueprint('nmap', __name__)


@app.route('/nmap', methods=['GET'])
@login_required
def nmap_view():
    try:
        print(retrieve_specs())

        return render_template('nmap.html')

    except Exception as e:
        logger.exception(e)
        return render_template('nmap.html')
