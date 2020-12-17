from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, FloatField, DecimalField, IntegerField, DateTimeField, FileField, \
    BooleanField, SubmitField
from wtforms.validators import Email, DataRequired


class SignupForm(FlaskForm):
    name = StringField(u'Your name', validators=[DataRequired()])
    password = StringField(u'Your favorite password', validators=[DataRequired()])
    email = StringField(u'Your email address', validators=[Email()])
    birthday = DateField(u'Your birthday')

    a_float = FloatField(u'A floating point number')
    a_decimal = DecimalField(u'Another floating point number')
    a_integer = IntegerField(u'An integer')

    now = DateTimeField(u'Current time',
                        description='...for no particular reason')
    sample_file = FileField(u'Your favorite file')
    eula = BooleanField(u'I did not read the terms and conditions',
                        validators=[DataRequired('You must agree to not agree!')])

    submit = SubmitField(u'Signup')
