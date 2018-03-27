import os

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'project_demo'
USERNAME = 'root'
PASSWORD = 'zxcvBnm123'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True

SECRET_KEY = os.urandom(24)
