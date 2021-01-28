from flask_login import login_required
from modules.Shared.Logger import logger
from flask import request, render_template, Blueprint
from modules.Nmap.controllers import retrieve_regions, get_costs, init_scan, test1, test2


app = Blueprint('nmap', __name__)


@app.route('/nmap', methods=['GET'])
@login_required
def nmap_view():
    try:
        return render_template('nmap.html', costs=get_costs(), regions=retrieve_regions())

    except Exception as e:
        logger.exception(e)
        return render_template('nmap.html', costs='', regions=[])


@app.route('/nmap/create', methods=['POST'])
@login_required
def nmap_init():
    try:
        print(request.get_json())
        # if not init_scan(request.get_json()):
        #     return '', 400

        return '', 200

    except Exception as e:
        logger.exception(e)
        return '', 500


@app.route('/test', methods=['GET'])
@login_required
def test():
    test1()

    return '', 200


@app.route('/test/delete/<droplet_id>', methods=['GET'])
@login_required
def test_delete(droplet_id):
    test2(droplet_id)

    return '', 200
