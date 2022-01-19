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


@application.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@application.route('/about/',  methods=['GET', 'POST'])
def about():
	return render_template('about.html')
	
@application.route('/tutorial/',  methods=['GET', 'POST'])
def tutorial():
	return render_template('tutorial.html')
	
@application.route('/contact/',  methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')


# from static.py.read_file import Read
# from static.py.extract_dates import Deadlines
# from static.py.output import Output
# @application.route('/start/')
# def tutorial():
# 	Read.read_func()
# 	Deadlines.deadlines_func()
# 	Output.output_func()
# 	return render_template('start.html')

# @application.route('/start/', methods=['POST'])
# def my_form_post():
# 	text = request.form['query']
# 	query = text.upper()
# 	print(query)
# 	return query

@application.route('/upload/',  methods=['GET', 'POST'])
def upload():
	return render_template('home.html')

from static.py.test import Test 			# from file.py import class
@application.route('/test/',  methods=['GET', 'POST'])
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

https://www.pexels.com/photo/composition-of-teapot-and-plant-twig-on-book-4271259/
https://www.pexels.com/photo/composition-of-white-mug-and-notebooks-4271257/
https://www.pexels.com/photo/notebooks-on-desk-with-ceramic-mug-4271258/

https://www.pexels.com/photo/ferns-and-flowers-surrounding-a-calendar-5498340/
https://www.pexels.com/photo/white-printer-paper-on-white-table-5499129/
https://www.pexels.com/photo/white-printer-paper-on-white-printer-paper-5498383/
https://www.pexels.com/photo/white-paper-on-green-table-5499139/

https://www.pexels.com/photo/close-up-shot-of-a-spiral-notebook-beside-a-cup-6690218/
https://www.pexels.com/photo/close-up-shot-of-a-pen-on-planner-6690208/
https://www.pexels.com/photo/flatlay-photo-of-weekly-planner-6690924/
https://www.pexels.com/photo/close-up-shot-of-weekly-planner-6690930/

https://www.svgrepo.com/svg/4336/calendar
https://realfavicongenerator.net/
'''
