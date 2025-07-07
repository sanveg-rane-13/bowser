from enum import Enum


class URL_TYPE(Enum):
    WEB = 1
    FILE = 2
    DATA = 3


class URL:
    default_file = "file:///Users/sanvegrane/Bowser/notes.txt"

    def __init__(self, url: str):
        self.__parse_url__(url)


    def __parse_url__(self, url: str):
        self.scheme, url = url.split("://", 1)

        if self.scheme == "file":
            """
            eg. file:///Users/sanvegrane/Bowser/notes.txt
            """
            self.type = URL_TYPE.FILE
            self.__parse_file_url__(url)
        
        elif self.scheme == "http" or self.scheme == "https":
            """
            eg. http://example.org/
            """
            self.type = URL_TYPE.WEB
            self.__parse_web_url__(url)

        else:
            raise Exception("Soweee... Bowser can't help you!")


    def __parse_file_url__(self, url: str):
        self.path = url

    
    def __parse_web_url__(self, url: str):
        self.host, url = url.split("/", 1)
        self.path = "/" + url

        if ":" in self.host:
            self.host, port = self.host.split(":", 1)
            self.port = int(port)

        elif self.scheme == "http": self.port = 80
        elif self.scheme == "https": self.port = 443

    
    def get_url_type(self) -> URL_TYPE:
        return self.type