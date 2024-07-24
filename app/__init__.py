from flask import Flask
from mongoengine import connect


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../.env')
    connect(db='rideNow', host='localhost', port=27017)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
