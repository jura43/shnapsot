from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from forms.password_checker import password_checker
from forms.username_checker import username_checker

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

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Username is required'), Length(min=3, message='Username must have at least 3 characteres'), usernameValid])
    password = PasswordField('Password', validators=[DataRequired('Password is required'), pwComplexity])
    password_repeat = PasswordField('Confirm Password', validators=[DataRequired('Please repeat the password'), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')