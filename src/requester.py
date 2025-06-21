from abc import ABC, abstractmethod

from url import URL

class Requester(ABC):
    @abstractmethod
    def request_url(self, url: URL, params: dict):
        pass