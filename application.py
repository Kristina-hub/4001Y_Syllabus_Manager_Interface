# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def index():
	return render_template('index.html')

from static.py.test import Test 			# from file.py import class
@application.route('/test/')
def test():
	return Test.test_func() 				# call function
	
'''
how to run locally:
export FLASK_APP="application.py"
flask run
command shift R to reload static files

references:
https://www.pexels.com/photo/clipboard-with-calendar-placed-on-desk-amidst-stationery-6408282/
https://www.pexels.com/photo/cup-of-fresh-cappuccino-near-laptop-keyboard-and-notebook-414645/
https://www.svgrepo.com/svg/4336/calendar
https://realfavicongenerator.net/
'''
