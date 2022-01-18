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

app = Flask(__name__)

@application.route('/')
def index():
	return Test.test_func()

# @application.route('/')
# def index():
# 	return render_template('index.html')

# @application.route('/upload', methods=['GET', 'POST'])
# def upload():
#     return render_template('upload.html')
    
'''
export FLASK_APP="application.py"
flask run
'''