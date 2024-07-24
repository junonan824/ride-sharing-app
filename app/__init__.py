from flask import Flask
from mongoengine import connect
from dotenv import load_dotenv
import os

def create_app(config_name='development'):
    app = Flask(__name__)
    load_dotenv()

    if config_name == 'testing':
        app.config['MONGO_URI'] = os.getenv('MONGO_URI_TEST')
    else:
        app.config['MONGO_URI'] = os.getenv('MONGO_URI')

    connect(host=app.config['MONGO_URI'])

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app