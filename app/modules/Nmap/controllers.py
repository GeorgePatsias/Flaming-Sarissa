from uuid import uuid4
from datetime import datetime
from flask_login import current_user
from modules.Shared.Logger import logger
from modules.Shared.DO import DigitalOcean
from modules.Profile.controllers import get_DO_token
from modules.Shared.MongoManager import mongo_connection
from config import MONGO_DB, MONGO_DO_COSTS_COLL, MONGO_USERS_COLL, MONGO_DO_REGIONS, MONGO_DO_PROJECTS

mongo_client = mongo_connection()
db = mongo_client[MONGO_DB]
users_collec = db[MONGO_USERS_COLL]
do_costs_collec = db[MONGO_DO_COSTS_COLL]
regions_collec = db[MONGO_DO_REGIONS]
projects_collec = db[MONGO_DO_PROJECTS]


def parse_regions(data):
    try:
        regions_list = []
        for region in data['regions']:
            if not region['available']:
                continue

            regions_list.append(region)

        return regions_list

    except Exception as e:
        logger.exception(e)
        return []


def retrieve_regions():
    try:
        regions_list = regions_collec.find_one({}, {'_id': 0})

        if regions_list:
            time_difference = datetime.now() - regions_list['createdAt']

            if time_difference.days <= 7:
                return parse_regions(regions_list)

        DO_client = DigitalOcean(get_DO_token(current_user.get_id()))

        regions_list = parse_regions(DO_client.list_regions())

        regions_collec.update({}, {'regions': regions_list, 'createdAt': datetime.now()}, upsert=True)

        return regions_list

    except Exception as e:
        logger.exception(e)
        return []


def get_costs():
    try:
        results = list(do_costs_collec.find({}, {"_id": 0}))

        result_html = """"""
        for server in results:
            row = """
                <tr>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td>{}</td>
                    <td><input type="radio" name="server_spec" data-price="{}" value="{}" /></td>
                </tr>
            """.format(
                server['memory'],
                server['cpu'],
                server['transfer'],
                server['ssd_disk'],
                server['cost'],
                server['cost'],
                server['value'],
            )

            result_html = result_html + row

        return result_html

    except Exception as e:
        logger.exception(e)
        return ''


def init_scan(data):
    try:
        if not data:
            return False

        for key, value in data.items():
            if key not in ['ip_list', 'server_distribution', 'nmap_parameters', 'do_server', 'regions_list'] or not value:
                return False

        ip_list = data['ip_list']
        server_distribution = data['server_distribution']
        nmap_parameters = data['nmap_parameters']
        do_server = data['do_server']
        regions_list = data['regions_list']

        DO_client = DigitalOcean(get_DO_token(current_user.get_id()))

        project_result = DO_client.create_project('Nmap')

        project_result = project_result.get('project', None)

        if not project_result:  # {'id': 'conflict', 'message': 'name is already in use (duplicate)'}  ALREADY EXISTS
            project_result = projects_collec.find_one({}, {'_id': 0})
        else:
            projects_collec.insert(project_result)


        return True

    except Exception as e:
        logger.exception(e)
        return False


# def start_scan(DO_client):
#     try:

#     except Exception as e:
#         logger.exception(e)


def test1():
    DO_client = DigitalOcean(get_DO_token(current_user.get_id()))

    p_res = DO_client.create_project()
    print(p_res)

    # drop_res = DO_client.create_droplet(str(uuid4()), "nyc3", "s-1vcpu-1gb", "ubuntu-20-04-x64")

    # print(drop_res)

    # urns = ["do:droplet:{}".format(drop_res['droplet']['id'])]

    # res = DO_client.assign_resources_project(p_res['project']['id'], urns)
    # print(res)

    return


def test2(id):
    DO_client = DigitalOcean(get_DO_token(current_user.get_id()))

    res = DO_client.delete_droplet_id(id)

    print(res)

    return
