from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    stunumber = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(11), nullable=False)

class Release(db.Model):
    __tablename__ = 'release'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('user',backref=db.backref('release'))
