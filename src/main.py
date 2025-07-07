import sys
import tkinter as tk

from url import URL, URL_TYPE

from file_requester import FileRequester
from web_requester import WebRequester
from window_renderer import WindowRenderer


class Bowser:
    '''
    The "Bowser" web browser

    eg1. python3 src/main.py http://example.org/index.html
    eg2. python3 src/main.py http://browser.engineering/examples/xiyouji.html
    '''
    def __init__(self):
        print("Welcome to Bowser, a browser meant to be very hostile!!")

        self.web_headers = {
            "Connection": "close",
            "User-Agent": "BOWSER"
        }

        self.web_requester = WebRequester()
        self.file_requester = FileRequester()
        self.window_renderer = WindowRenderer()

    
    def launch_bowser_for_url(self, url: str):
        # bring content from URL
        content = self.__request_page_contents__(url)

        if content:
            # render content on canvas
            self.window_renderer.load_webpage(content)
        else:
            print("Whoops... something went wrong ;(")

        # launch Bowser mainloop
        self.window_renderer.launch_window()


    def __request_page_contents__(self, user_url: str):
        try:
            url = URL(user_url)

            if url.get_url_type() == URL_TYPE.FILE:
                requester = self.file_requester
            else:
                requester = self.web_requester

            # defaults to WEB requester
            return requester.request_url(url, self.web_headers)

        except Exception as e:
            # TODO: render exception is some error
            print(e)



if __name__ == "__main__":
    bowser = Bowser()
    bowser.launch_bowser_for_url(sys.argv[1])