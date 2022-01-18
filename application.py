# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #


from flask import Flask, render_template, request, url_for, redirect
application = Flask(__name__)


@application.route('/')
def menu():
	return render_template('menu.html')
	

from static.py.read_file import Read
from static.py.extract_dates import Deadlines
from static.py.output import Output
@application.route('/start/')
def start():
	Read.read_func()
	Deadlines.deadlines_func()
	Output.output_func()
	return render_template('start.html')


@application.route('/start/', methods=['POST'])
def my_form_post():
	text = request.form['query']
	query = text.upper()
	print(query)
	return query


from static.py.test import Test 			# from file.py import class
@application.route('/test/')
def test():
	return Test.test_func() 				# call function
	
	
'''
how to run locally:
export FLASK_APP="application.py"
flask run
http://127.0.0.1:5000/
command shift R to reload static files

references:
https://www.pexels.com/photo/clipboard-with-calendar-placed-on-desk-amidst-stationery-6408282/
https://www.pexels.com/photo/cup-of-fresh-cappuccino-near-laptop-keyboard-and-notebook-414645/
https://www.svgrepo.com/svg/4336/calendar
https://realfavicongenerator.net/
'''
