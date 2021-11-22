#!/Users/admin/anaconda/bin/python3
import uuid
import datetime
from time import sleep
import os, os.path
from http.server import HTTPServer, BaseHTTPRequestHandler 
import requests

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler): 
  
  configText=""

  def readFile(self):

    while not os.path.exists("/tmp/kube/ping.txt"):
      sleep(5)
    
    with open("/tmp/kube/ping.txt","r") as f:
       return(f.readline())

  def fetchPing(self):
    ping=requests.get("http://pingpong-svc:5563/pingpong")
    return str(ping.text)

  def readConfigmap(self,key):
      return str(os.getenv(key, 0))


  def do_GET(self):
    self.send_response(200) 
    self.end_headers() 
    #line= f"<p>{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}  {str(uuid.uuid4())}</p></br>" + self.readFile()
    line= self.readConfigmap("MESSAGE") + f"</br><p>{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}  {str(uuid.uuid4())}</p></br>" + self.fetchPing()
    self.wfile.write(line.encode("utf-8"))



httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()