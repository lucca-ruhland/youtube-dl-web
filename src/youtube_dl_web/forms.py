from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, SubmitField
from wtforms.validators import URL, data_required


class DownloadForm(FlaskForm):
    url = StringField(u'enter your youtube URL', validators=[URL()])
    download_format = SelectField(label='download format', choices=[('mp3', '.mp3 (audio)'), ('mp4', '.mp4 (video)')],
                                  validators=[data_required()])

    submit = SubmitField(u'download')
