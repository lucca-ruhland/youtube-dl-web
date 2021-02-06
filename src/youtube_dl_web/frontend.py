import glob
import os
import pathlib
from zipfile import ZipFile

from flask import Blueprint, render_template, send_from_directory
from flask_bootstrap import __version__ as flask_bootstrap_version
from flask_nav.elements import Navbar, View, Text

from youtube_dl_web.forms import DownloadForm
from youtube_dl_web.nav import nav
from youtube_dl_web.ydl_helper import YoutubeDownloadHandler

frontend = Blueprint('frontend', __name__)

nav.register_element('frontend_top', Navbar(
    View('Youtube-DL-web', 'frontend.index'),
    View('Home', 'frontend.index'),
    View('Download', 'frontend.download'),
    View('Debug-Info', 'debug.debug_root'),
    Text('Using Flask-Bootstrap {}'.format(flask_bootstrap_version)),
))


@frontend.after_app_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'

    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')

    return response


@frontend.route('/')
def index():
    return render_template('index.html')


@frontend.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.png')


@frontend.route('/downloads/', methods=('GET', 'POST'))
def download():
    form = DownloadForm()

    if form.validate_on_submit():
        handler = get_handler()

        url_list = form.url.data
        download_format = form.download_format.data.lstrip('.')
        download_files(handler, url_list, download_format)

        download_dir = get_directory(handler)
        files = get_file_path(download_dir)

        if len(files) == 1:
            return send_from_directory(str(download_dir), files[0], as_attachment=True)
        else:
            zip_name = 'download.zip'
            zip_path = download_dir.joinpath(zip_name)
            zip_object = ZipFile(zip_path, 'w')

            for file in files:
                zip_object.write(download_dir.joinpath(file), arcname=file)

            zip_object.close()
            return send_from_directory(str(download_dir), zip_name, as_attachment=True)

    return render_template('download.html', form=form)


def get_handler() -> YoutubeDownloadHandler:
    handler = YoutubeDownloadHandler.default()
    return handler


def get_directory(handler: YoutubeDownloadHandler) -> pathlib.Path:
    download_dir = pathlib.Path(handler.temp_dir.name).joinpath('Youtube/')
    return download_dir


def download_files(handler: YoutubeDownloadHandler, url_list_as_str: str, download_format: str):
    url_list = url_list_as_str.split('\n')
    for url in url_list:
        handler.download(url, download_format)


def get_file_path(download_dir: pathlib.Path) -> list:
    download_dir = str(download_dir)

    files = map(os.path.basename, glob.glob(download_dir + f'/*.*'))
    files = list(files)
    return files
