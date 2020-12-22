import json
import requests
from uuid import uuid4
from config import DIGITAL_OCEAN_TOKEN


class DigitalOcean:
    def __init__(self):
        self.token = DIGITAL_OCEAN_TOKEN

    def create_droplet(self):
        try:
            return requests.post(
                "https://api.digitalocean.com/v2/droplets",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                },
                data={
                    "name": str(uuid4()),
                    "region": "nyc3",
                    "size": "s-1vcpu-1gb",
                    "image": "ubuntu-16-04-x64",
                    "ssh_keys": [107149],
                    "backups": False,
                    "ipv6": False,
                    "user_data": None,
                    "private_networking": None,
                    "volumes": None,
                    "tags": ["web"]
                }
            ).json()

        except Exception:
            return {}

    def get_droplet(self, id):
        try:
            return requests.get(
                "https://api.digitalocean.com/v2/droplets/{}".format(id),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                }
            ).json()

        except Exception:
            return {}

    def delete_droplet(self, id):
        try:
            return requests.delete(
                "https://api.digitalocean.com/v2/droplets/{}".format(id),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                }
            ).json()

        except Exception:
            return {}

    def list_droplets(self):
        try:
            return requests.get(
                "https://api.digitalocean.com/v2/droplets",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                }
            ).json()

        except Exception:
            return {}

    def get_ssh_key(self, id):
        try:
            return requests.get(
                "https://api.digitalocean.com/v2/account/keys/{}".format(id),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                }
            ).json()

        except Exception:
            return {}

    def rename_ssh_key(self, id, name):
        try:
            return requests.put(
                "https://api.digitalocean.com/v2/account/keys/{}".format(id),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                },
                data={
                    "name": name
                }
            ).json()

        except Exception:
            return {}

    def delete_ssh_key(self, id):
        try:
            return requests.delete(
                "https://api.digitalocean.com/v2/account/keys/{}".format(id),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                }
            ).json()

        except Exception:
            return {}

    def insert_ssh_key(self, name, key):
        try:
            return requests.post(
                "https://api.digitalocean.com/v2/account/keys",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                },
                data={
                    "name": name,
                    "public_key": key
                }
            ).json()

        except Exception:
            return {}

    def list_ssh_keys(self):
        try:
            return requests.get(
                "https://api.digitalocean.com/v2/account/keys",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                }
            ).json()

        except Exception:
            return {}

    def list_regions(self):
        try:
            return requests.get(
                "https://api.digitalocean.com/v2/regions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(self.token)
                }
            ).json()

        except Exception:
            return {}