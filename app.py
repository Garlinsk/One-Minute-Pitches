from flask import Flask

# create an instace of my app
app = Flask(__name__)


@app.route('/')
def home():


     return "Lets build Pitches"


if __name__ == '__main__':
    app.run(debug=True)