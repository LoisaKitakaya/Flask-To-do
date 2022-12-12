from flask import Flask

from config import Config

def create_app(config_object=Config):

    app = Flask(__name__)
    app.config.from_object(config_object)

    # initialize extensions

    # register blueprints

    @app.route('/test/')
    def test_route():

        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app