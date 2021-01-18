from flask import Blueprint, render_template, flash, redirect, url_for, current_app, send_from_directory
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Text
from markupsafe import escape

from youtube_dl_web.forms import DownloadForm
from youtube_dl_web.nav import nav

import pathlib
import glob
import os

frontend = Blueprint('frontend', __name__)

nav.register_element('frontend_top', Navbar(
    View('Youtube-DL-web', 'frontend.index'),
    View('Home', 'frontend.index'),
    View('download', 'frontend.example_form'),
    View('Debug-Info', 'debug.debug_root'),
    Text('Using Flask-Bootstrap {}'.format(FLASK_BOOTSTRAP_VERSION)),
))


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/example-form/', methods=('GET', 'POST'))
def example_form():
    form = DownloadForm()

    if form.validate_on_submit():
        flash('You have successfully downloaded {} !'
              .format(escape(form.url.data)))

        url = form.url.data
        download_format = form.download_format.data.lstrip('.')

        handler = current_app.config['HANDLER']
        handler.download(url, download_format)

        download_dir = pathlib.Path(handler.temp_dir.name).joinpath('Youtube/')
        download_dir = str(download_dir)

        files = map(os.path.basename, glob.glob(download_dir + f'/*.*'))

        for file in files:
            return send_from_directory(download_dir, file, as_attachment=True)

        return redirect(url_for('frontend.index'))

    return render_template('download.html', form=form)


