from flask import Flask, render_template

# import forms
from forms import loginForm, signupForm

# create an instace of my app
app = Flask(__name__)
app.config["SECRET_KEY"] = "mbogiyapython"



@app.route('/')
def home():

    return render_template('index.html')

@app.route('/login')
def login():

    form = loginForm()

    return render_template('login.html',form=form)


@app.route('/singup')
def signup():

    return render_template('signup.html')


@app.route('/my_schedule')
def my_schedule():
    return render_template('my_schedule.html')


if __name__ == '__main__':
    app.run(debug=True)
