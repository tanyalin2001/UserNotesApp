from . import db
#from this package, we can import anything in init.py
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now()) #func gets the current date and time
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #in sql, foreign key we use lower case

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(150), unique = True)
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))
  notes = db.relationship('Note') #relationship -> reference(whatever it's lower case or upper case)
