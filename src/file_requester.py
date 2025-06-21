import os

from requester import Requester
from url import URL, URL_TYPE

class FileRequester(Requester):
    def __init__(self):
        pass

    def request_url(self, url: URL, params: dict):
        assert url.get_url_type() == URL_TYPE.FILE

        if os.path.isdir(url.path):
            entries = os.listdir(url.path)

            print(f"Entries in '{url.path}':")
            for entry in entries:
                print(entry)

        else:
            file = open(url.path, "r")
            content = file.read()
            file.close()

            print(content)
