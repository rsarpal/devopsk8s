from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#making table Words
class CounterTable(db.Model):
    __tablename__ = 'CounterTable'
    # making table's columns
    id = db.Column(db.Integer,primary_key=True) # making table's id a table cannot be made without an id
    counter = db.Column(db.Integer)

    def __repr__(self):
        return '<Counter %r>' % self.counter