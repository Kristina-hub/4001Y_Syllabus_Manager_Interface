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

# from static.py.test import Test 			# from file.py import class
# @application.route('/test/')
# def test():
# 	return Test.test_func() 				# call function
	
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

public links:
AWS -> Services -> Elastic beanstalk
Create New Application called hack-western-8 using Python
Create New Environment called hack-western-8-env using Web Server Environment

Services -> Developer Tools -> CodePipeline
Create Pipeline called hack-western-8
GitHub Version 2 -> Connect to Github
Connection Name -> Install a New App -> Choose Repo Name -> Skip Build Stage -> Deploy to AWS Elastic Beanstalk

This link is no longer local:
syllabi-env.eba-knxutzu2.us-east-1.elasticbeanstalk.com
http://syllabi-env.eba-knxutzu2.us-east-1.elasticbeanstalk.com/
52.205.181.195
54.227.40.144

Route 53 -> Registered Domains -> Register Domain -> hack-western-8.com -> Check
Route 53 -> Hosted zones -> Create Record -> Route Traffic to IPv4 Address -> Alias -> Elastic Beanstalk -> hack-western-8-env -> Create Records
Create another record but with alias www.

syllabi.ca
www.syllabi.ca
http://syllabi.ca
http://www.syllabi.ca/

AWS Certificate Manager -> Request a Public Certificate -> Domain Name "hack-western-8.com" and "*.hack-western-8.com" -> DNS validation -> Request
$ dig +short CNAME -> No Output? -> Certificate -> Domains -> Create Records in Route 53
Elastic Beanstalk -> Environments -> Configuration -> Capacity -> Enable Load Balancing
Load balancer -> Add listener -> Port 443 -> Protocol HTTPS -> SSL certificate -> Save -> Apply

https://syllabi.ca
https://syllabi.ca
'''
