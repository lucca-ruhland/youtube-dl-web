from flask import Flask
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap
from flask_debug import Debug

from youtube_dl_web.frontend import frontend
from youtube_dl_web.nav import nav


def create_app(test_config=None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    AppConfig(app, test_config)

    Debug(app)

    Bootstrap(app)

    app.register_blueprint(frontend)
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    nav.init_app(app)

    return app
