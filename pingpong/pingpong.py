#!/Users/admin/anaconda/bin/python3
from flask import Flask

count=0

def writeFile(count):
  with open("/tmp/kube/ping.txt","w") as f:
    f.write("Ping / Pongs: " + str(count))

def create_app():
    app = Flask(__name__)

    @app.route('/pingpong')
    def pingpong():
        global count
        count += 1
        #print (str(count))
        writeFile(count)
        return f"{count:d}"



    if __name__ == "__main__":
        app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))

    return app