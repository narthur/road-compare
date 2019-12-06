import requests


class Requests:
    @staticmethod
    def get_json(url):
        return requests.get(url).json()
