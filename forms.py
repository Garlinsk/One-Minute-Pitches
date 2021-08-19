from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired,Email,Length

# login form
class loginForm(FlaskForm):
    username= StringField('username', validators=[InputRequired(),Length(min=4,max=16)])
    Password= PasswordField('password', validators=[InputRequired(),Length(min=8,max=85)])
    remember=BooleanField('remember me')

# sign up form
class signupForm(FlaskForm):
    first_name= StringField('first_name', validators=[InputRequired(),Length(min=4,max=16)])
    last_name= StringField('last-name', validators=[InputRequired(),Length(min=4,max=16)])
    username= StringField('username', validators=[InputRequired(),Length(min=4,max=16)])
    email= StringField('email', validators=[InputRequired(),Email(message='invalid email'),Length(max=60)])
    password= PasswordField('password', validators=[InputRequired(),Length(min=8,max=85)])