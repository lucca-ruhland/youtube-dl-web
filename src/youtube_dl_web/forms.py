from flask_wtf import FlaskForm
from wtforms.fields import SelectField, SubmitField, TextAreaField
from wtforms.validators import URL, data_required, input_required

from youtube_dl_web.ydl_helper import YTDownloadFormat

available_formats = [(dl_format.name, dl_format.name) for dl_format in YTDownloadFormat]


class DownloadForm(FlaskForm):
    url = TextAreaField(u'enter your youtube URL', validators=[input_required()])
    download_format = SelectField(label='download format', choices=available_formats,
                                  validators=[data_required()])

    @staticmethod
    def validate_url(form, field):
        url_list = field.data.split('\n')

        try:
            for url in url_list:
                assert URL().validate_hostname(url)
        except AssertionError:
            return False

        return True

    submit = SubmitField(u'download')
