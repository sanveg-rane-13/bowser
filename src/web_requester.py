import socket
import ssl

from requester import Requester
from threading import Lock
from url import URL, URL_TYPE

class WebRequester(Requester):

    def __init__(self) -> None:
        self.conn_lock = Lock()

        self.ctx = ssl.create_default_context()
        self.soc = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=socket.IPPROTO_TCP)

        self.scheme_map = {
            "http"  : "HTTP/1.1",
            "https" : "HTTPS"
        }


    def request_url(self, url: URL, params: dict):
        assert url.get_url_type == URL_TYPE.WEB

        req = f"GET {url.path} {self.scheme_map[url.scheme]}\r\n"
        
        if "Host" not in headers:
            req += f"Host: {url.host}\r\n"
        
        for key, val in headers.items():
            req += f"{key}: {val}\r\n"
        req += "\r\n"

        response = None

        with self.conn_lock:
            if url.scheme == "https":
                secure_conn = self.ctx.wrap_socket(self.soc, server_hostname=url.host)
            else:
                secure_conn = self.soc
            
            secure_conn.connect((url.host, url.port))

            print(f"Sending request: {req}")
            secure_conn.send(req.encode("utf8"))
            response = secure_conn.makefile("r", encoding="utf8", newline="\r\n")
            secure_conn.close()
        
        if response is not None:
            self.inspect_headers(response)
            content = response.read()
            self.show(content)


    def inspect_headers(self, response):
        statusline = response.readline()
        version, status, explanation = statusline.split(" ", 2)

        response_headers = {}
        while True:
            line = response.readline()
            if line == "\r\n": break
            header, value = line.split(":", 1)
            response_headers[header.casefold()] = value.strip()

        assert "transfer-encoding" not in response_headers
        assert "content-encoding" not in response_headers

        print(f"Received response with status = {status}")

    
    def show(self, body):
        in_tag = False

        for ch in body:
            if ch == "<":
                in_tag = True
            
            elif ch == ">":
                in_tag = False
            
            elif not in_tag:
                print(ch, end="")