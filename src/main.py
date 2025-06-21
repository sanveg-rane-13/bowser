import sys

from url import URL, URL_TYPE

from file_requester import FileRequester
from web_requester import WebRequester


class Bowser:
    def __init__(self):
        print("Welcome to Bowser, an browser meant to be very hostile!!")

        self.web_headers = {
            "Connection": "close",
            "User-Agent": "BOWSER"
        }

        self.web_requester = WebRequester()
        self.file_requester = FileRequester()

    
    def request_page(self, url: str):
        try:
            user_url = URL(url)
            self.__handle_bowser_url__(user_url)

        except Exception as e:
            print(e)
            

    def __handle_bowser_url__(self, url: URL):
        if url.get_url_type() == URL_TYPE.WEB:
            self.web_requester.request_url(url, self.web_headers)
        elif url.get_url_type() == URL_TYPE.FILE:
            self.file_requester.request_url(url, self.web_headers)



if __name__ == "__main__":
    bowser = Bowser()
    bowser.request_page(sys.argv[1])