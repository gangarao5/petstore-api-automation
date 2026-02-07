import requests

class BaseClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        return requests.get(self.base_url + endpoint, params=params)

    def post(self, endpoint, json=None):
        return requests.post(self.base_url + endpoint, json=json)

    def put(self, endpoint, json=None):
        return requests.put(self.base_url + endpoint, json=json)

    def delete(self, endpoint):
        return requests.delete(self.base_url + endpoint)
