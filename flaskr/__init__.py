import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    Bootstrap(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return render_template("index.html")

    from . import robot
    app.register_blueprint(robot.bp)

    return app

