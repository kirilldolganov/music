class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://UserOne:password@localhost/music'