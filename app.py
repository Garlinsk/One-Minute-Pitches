from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from configs.base_config import *


# import forms
from forms import loginForm, signupForm

# create an instace of my app
app = Flask(__name__)

app.config.from_object(Development)

db = SQLAlchemy(app)

# import models
from models.user import User

# @app.before_first_request
# def create_tables():
#     db.create_all()


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():

    form = loginForm()

    # check for validation
    if form.validate_on_submit():
        print("username", form.username.data, "password", form.password.data)

    return render_template('login.html', form=form)


@app.route('/singup')
def signup():

    form = signupForm()

    # get data
    # send data to a db

    return render_template('signup.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
