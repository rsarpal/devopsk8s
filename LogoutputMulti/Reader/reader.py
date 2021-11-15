from http.server import HTTPServer, BaseHTTPRequestHandler 
from time import sleep
import os.path

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler): 

  def readfile(self):
    line = ""

    while not os.path.exists("files/file.txt"):
      sleep(5)

    with open("files/file.txt","r") as f:
      for i in f:
        line= line + f.readline() + "\n"
        print (line)
    return line

  def do_GET(self):
    self.send_response(200) 
    self.end_headers() 
    self.wfile.write(self.readfile().encode("utf-8"))

httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()