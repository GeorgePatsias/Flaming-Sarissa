from modules.Shared.Logger import logger
from modules.Shared.DO import DigitalOcean


def retrieve_specs():
    try:
        DO_client = DigitalOcean()

        results = DO_client.list_regions()

        regions_list = []
        for res in results['regions']:
            if res['available'] == False:
                continue

            regions_list.append(res['name'])

        return regions_list

    except Exception as e:
        logger.exception(e)
        return None
