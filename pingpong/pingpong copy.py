#!/Users/admin/anaconda/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Counter

class Pingpong(BaseHTTPRequestHandler):
    """docstring for Pingpong."""

    #def __init__(self):
    #    super(Pingpong, self).__init__()
    #    self.counter =0

    

    def do_GET(self):
        global count
        count = count + 1
        self.send_response(200)
        self.end_headers
        self.wfile.write(f"{self.counter}")

httpd = HTTPServer(('localhost', 8004), Pingpong)
httpd.serve_forever()