from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/upload')
def upload():
    return render_template('upload.html')

# export FLASK_APP="application.py"
# flask run