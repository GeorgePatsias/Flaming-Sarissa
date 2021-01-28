import json
import requests
from uuid import uuid4
from modules.Shared.Logger import logger
from config import DIGITAL_OCEAN_URL, DIGITAL_OCEAN_PROJECT_NAME


class DigitalOcean:
    def __init__(self, token):
        self.token = token
        self.url = DIGITAL_OCEAN_URL
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }

    def create_droplet(self, name, region, size, image):
        try:
            return requests.post(
                '{}/droplets'.format(self.url),
                headers=self.headers,
                data=json.dumps({
                    'name': name,
                    'region': region,
                    'size': size,
                    'image': image,
                    'tags': ['test']
                })
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def create_multiple_droplets(self, names, region, size, image):
        try:
            return requests.post(
                '{}/droplets'.format(self.url),
                headers=self.headers,
                data=json.dumps({
                    'names': names,
                    'region': region,
                    'size': size,
                    'image': image
                })
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def retrieve_droplet_by_id(self, id):
        try:
            return requests.get(
                '{}/droplets/{}'.format(self.url, id),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def list_all_droplets(self):
        try:
            return requests.get(
                '{}/droplets'.format(self.url),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def list_all_droplets_by_tag(self, tag):
        try:
            return requests.get(
                '{}/droplets?tag_name={}'.format(self.url, tag),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def list_actions_for_droplet(self, id):
        try:
            return requests.get(
                '{}/droplets/{}/actions'.format(self.url, id),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def delete_droplet_id(self, id):
        try:
            return requests.delete(
                '{}/droplets/{}'.format(self.url, id),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def delete_droplet_tag(self, tag):
        try:
            return requests.delete(
                '{}/droplets?tag_name={}'.format(self.url, tag),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def list_ssh_keys(self):
        try:
            return requests.get(
                '{}/account/keys'.format(self.url),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def create_new_ssh_key(self, name, key):
        try:
            return requests.post(
                '{}/account/keys'.format(self.url),
                headers=self.headers,
                data=json.dumps({
                    'name': name,
                    'public_key': key
                })
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def update_ssh_key(self, id, name, key):
        try:
            return requests.post(
                '{}/account/keys/{}'.format(self.url, id),
                headers=self.headers,
                data=json.dumps({
                    'name': name,
                    'public_key': key
                })
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def remove_ssh_key(self, id):
        try:
            return requests.delete(
                '{}/account/keys/{}'.format(self.url, id),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def list_regions(self):
        try:
            return requests.get(
                '{}/regions'.format(self.url),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def create_project(self, purpose):
        try:
            return requests.post(
                '{}/projects'.format(self.url),
                headers=self.headers,
                data=json.dumps({
                    'name': DIGITAL_OCEAN_PROJECT_NAME,
                    'purpose': purpose,
                    'environment': 'Production'
                })
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def assign_resources_project(self, id, droplet_urns):
        try:
            return requests.post(
                '{}/projects/{}/resources'.format(self.url, id),
                headers=self.headers,
                data=json.dumps({
                    'resources': droplet_urns
                })
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def list_all_projects(self):
        try:
            return requests.get(
                '{}/projects'.format(self.url),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def retrieve_project(self, id):
        try:
            return requests.get(
                '{}/projects/{}'.format(self.url, id),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}

    def delete_project(self, id):
        try:
            return requests.delete(
                '{}/projects/{}'.format(self.url, id),
                headers=self.headers
            ).json()

        except Exception as e:
            logger.exception(e)
            return {}
