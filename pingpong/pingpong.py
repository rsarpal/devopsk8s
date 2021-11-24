#!/Users/admin/anaconda/bin/python3
from typing import Counter
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.models import CounterTable, db
import os



count=0

def writeFile(count):
  with open("/tmp/kube/ping.txt","w") as f:
    f.write("Ping / Pongs: " + str(count))

def readConfigmap(key):
    return str(os.getenv(key, 0))

def writeDB(count):
    newCounter=CounterTable(counter=count)
    # adding new word to DB
    db.session.add(newCounter)
    db.session.commit()

    # latestCounter=CounterTable.query.all()
    # return latestCounter


def create_app():
    app = Flask(__name__)

    # Set DB settings
    #app.config['SECRET_KEY']= os.urandom(256)
    #"postgresql://<username>:<password>@<server>:5432/<db_name>"
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:' + readConfigmap("POSTGRES_PASSWORD") + '@postgres-db-svc:5432/' + readConfigmap("POSTGRES_DB")
    #app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:mysecretpassword@localhost:5432/counterdb'
    app.config['SQLALCHEMY_ECHO'] = True
    

    db.init_app(app)
    db.app = app
    db.create_all()

    @app.route('/pingpong')
    def pingpong():
        global count
        count += 1
        #print (str(count))
        #writeFile(count)
        writeDB(count)
        return f"{count:d}" 
        #+ str(writeDB(count))



    if __name__ == "__main__":
        app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))

    return app