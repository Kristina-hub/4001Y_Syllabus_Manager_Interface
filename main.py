from flask import Flask, render_template

#application = Flask(__name__)
#@application.route('/')
app = Flask(__name__)
@app.route("/")

# def hello_world():
# 	return 'Hello World'

def index():
    return render_template('index.html')