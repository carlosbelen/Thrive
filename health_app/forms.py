from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email

# DataRequired == Making sure the field is filled in
# EqualTo == Making sure the field(s) are the same (ie Password and Confirm Password)
# Email == Making sure the field has a proper email given to it

# Below:
# inherits information from WTF and secetkey
class UserInfoForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    # equal to 'password' is confirming the users inputed password. lowercase p to equal the name password 2 lines above
    submit = SubmitField()
    # this class funcition will be used in Routes.py where it'll be instantiated.

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField()