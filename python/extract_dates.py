# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

import re
		
class ExtractDates():

	def dates_func(text):
		print("Enter: deadlines_func.py")
		message = "Dates:<br/>"
		matches = []
	
		'''YYYY-MM-DD'''
		matches += re.findall(r'\d{4}-\d{2}-\d{2}', text)
	
		'''Month DD, YYYY'''
		'''Month D, YYYY'''
		'''Month D-D, YYYY'''
		'''Month DD-DD, YYYY'''
		'''Month DD'''
		'''Month D'''
		dates = re.findall(r'((Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2})(?:–\d{1,2})?(?:,)?(?:\s+(\d{4}))?)', text)
		[matches.append(x[0]) for x in dates]

		'''MM/DD'''
		'''MM/D'''
		'''M/D'''
		'''M/DD'''
		matches += re.findall(r'\d{1,2}\/\d{1,2}', text)

		'''MM/DD/YY'''
		'''MM/DD/YYYY'''
		'''DD/MM/YY'''
		'''DD/MM/YYYY'''
		matches += re.findall(r'\d{1,2}\/\d{1,2}\/(\d{4}|\d{2})', text)

		for match in matches:
			message += match
			message += "<br/>"

		print(matches)
		print("Exit: deadlines_func.py")
		return message



