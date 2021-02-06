import pathlib

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debug import Debug
from flask_wtf import CSRFProtect

from youtube_dl_web.default_config import Config
from youtube_dl_web.frontend import frontend
from youtube_dl_web.nav import nav


def create_app(test_config=None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        user_config = pathlib.Path('config.py')
        if user_config.exists():
            app.config.from_pyfile(user_config, silent=True)
        else:
            app.config.from_object(Config)
    else:
        app.config.from_object(test_config)

    Debug(app)

    Bootstrap(app)

    app.register_blueprint(frontend)
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True

    nav.init_app(app)

    crsf = CSRFProtect()
    crsf.init_app(app)

    return app
