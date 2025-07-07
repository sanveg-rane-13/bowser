import os

from requester import Requester
from url import URL, URL_TYPE

class FileRequester(Requester):
    def __init__(self):
        pass

    
    def request_url(self, url: URL, params: dict) -> str:
        assert url.get_url_type() == URL_TYPE.FILE
        content = ""
        if os.path.isdir(url.path):
            entries = os.listdir(url.path)

            content += f"Entries in '{url.path}': \n"
            for entry in entries:
                content += f"{entry}\n"

        else:
            content += "\n"
            file = open(url.path, "r")
            content += file.read()
            file.close()

        return content
