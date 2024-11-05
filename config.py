import os

class Config(): 
    CSRF_ENABLE = True
    SECRET = "nijvnvibefjrnierbogijnsid"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None
    
class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = 8000
    URL_MAIN = "http:/%s/%s" % (IP_HOST, PORT_HOST) # http://localhost:8000
    SQLALCHEMY_DATABASE_URI="postgresql://iran:root@localhost:5432/dash?schema=public"

app_config = {
    "development" : DevelopmentConfig(),
}

app_active = os.getenv("FLASK_ENV")
if app_active is None:
    app_active = "development"




""" class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    IP_HOST = "colocar depois"
    PORT_HOST = 8080
    URL_MAIN = "http:/%s/%s" % (IP_HOST, PORT_HOST) # http://localhost:8000
    SQLALCHEMY_DATABASE_URI = "a colocar"
    
class ProductionConfig(Config):
    DEBUG = False
    TESTING = True
    IP_HOST = "colocar depois"
    PORT_HOST = 8080
    URL_MAIN = "http:/%s/%s" % (IP_HOST, PORT_HOST) # http://localhost:8000
    SQLALCHEMY_DATABASE_URI = "a colocar" """
