import os
import pprint
import sys
from time import sleep

from flask import Flask
from flask_uuid import FlaskUUID

API_PREFIX = '/1'


def load_config(app):

    config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'config.py')
    app.config.from_pyfile(config_file)

    try:
        with open('.git-version') as git_version_file:
            print('Running on git commit: %s' % git_version_file.read().strip())
    except IOError as e:
        print('Unable to retrieve git commit. Error: %s', str(e))


def gen_app(config_path=None, debug=None):
    """ Generate a Flask app for Hind with all configurations done and connections established.
    In the Flask app returned, blueprints are not registered.
    """
    app = Flask(import_name=__name__)
    FlaskUUID(app)

    load_config(app)

    # Database connections
    from hind import db
    db.init_db_connection(app.config['SQLALCHEMY_DATABASE_URI'])

    # Error handling
    from hind.webserver.errors import init_error_handlers
    init_error_handlers(app)

    return app


def create_app(config_path=None):

    app = gen_app(config_path=config_path)

    # Static files
    from hind.webserver import static_manager
    static_manager.read_manifest()
    app.context_processor(lambda: dict(get_static_path=static_manager.get_static_path))
    app.static_folder = '/static'

    # _register_blueprints(app)

    return app


def _register_blueprints(app):
    from hind.webserver.views.index import index_bp
    from hind.webserver.views.login import login_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(login_bp, url_prefix='/login')
