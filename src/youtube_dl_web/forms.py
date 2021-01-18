from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, SubmitField
from wtforms.validators import URL, data_required

from youtube_dl_web.ydl_helper import YTDownloadFormat


available_formats = [(dl_format.name, dl_format.name) for dl_format in YTDownloadFormat]


class DownloadForm(FlaskForm):
    url = StringField(u'enter your youtube URL', validators=[URL()])
    download_format = SelectField(label='download format', choices=available_formats,
                                  validators=[data_required()])

    submit = SubmitField(u'download')
