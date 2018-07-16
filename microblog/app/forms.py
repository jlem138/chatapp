from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usernadme', validators = [DataRequired()])
    password = PasswordField('Pasadfsword', validators = [DataRequired()])
    remember_me = BooleanField('Rememadfber Me')
    ex = BooleanField('Example')
    submit = SubmitField('dfd In')
