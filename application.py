# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

from flask import Flask, render_template
from static.py.test import Test #from file.py import class
import os

app = Flask(__name__)
# app._static_folder = os.path.abspath("static/")

# @application.route('/')
@app.route('/')
def index():
	return Test.test_func()

# @application.route('/')
# def index():
# 	return render_template('index.html')

# @application.route('/upload', methods=['GET', 'POST'])
# def upload():
#     return render_template('upload.html')

# if __name__ == "__main__":
#     print("test")

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0',port=5000) 
    
    
'''
export FLASK_APP="application.py"
export FLASK_APP="main.py"
flask run
'''