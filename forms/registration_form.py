from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from forms.password_checker import password_checker
from forms.username_checker import username_checker
from website import db
from models.model import Users

def pwComplexity(form, field):
    password = password_checker(field.data)
    if password['length_error'] == True:
        raise ValidationError('Password need to be at least 8 characthers long')
    elif password['password_ok'] == False:
        raise ValidationError('Password needs to contain upper and lower case letters, at least one symbol, and at least one digit')
    else: 
        pass

def usernameValid(form, field):
    if username_checker(field.data) is True:
        raise ValidationError('Username can contain only letters and numbers')

def usernameExists(form, field):
    username = Users.query.filter_by(username=field.data).first() is not None
    if username:
        raise ValidationError('Username already exists')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Username is required'), Length(min=3, message='Username must have at least 3 characters'), Length(max=9, message='Username cannot have more than 9 characters'), usernameValid, usernameExists])
    password = PasswordField('Password', validators=[DataRequired('Password is required'), pwComplexity])
    password_repeat = PasswordField('Confirm Password', validators=[DataRequired('Please repeat the password'), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')