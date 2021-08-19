from flask import Flask,render_template

# create an instace of my app
app = Flask(__name__)


@app.route('/')
def home():
     return render_template('index.html')


@app.route('/login') 
def login():
    return render_template('login.html')


@app.route('/singup') 
def signup():
    return render_template('signup.html')

@app.route('/my_schedule') 
def my_schedule():
    return render_template('my_schedule.html') 

if __name__ == '__main__':
    app.run(debug=True)