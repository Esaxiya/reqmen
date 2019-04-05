import os

DEBUG = True

# Session中使用、盐成分用于混入
SECRET_KEY = os.urandom(24)

# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'reqmen'
USERNAME = 'root'
PASSWORD = 'root'
# DB_URI ='mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format( USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE )
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True
