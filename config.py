import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgres://rtakasu:TYgEuErh@soccer-database.conqzky6vos0.us-west-2.rds.amazonaws.com:5432/postgres'

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	Debug = True