# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

import re
from dateutil.parser import parse
from datetime import datetime
import pandas as pd

class ExtractDates:

	def dates_func(text, filename):
		print("Enter: deadlines_func.py")

		'''Type: Assignment/Test/Project/Final/Midterm'''
		df = pd.DataFrame(columns=['File', 'Course', 'Deliverable', 'Date'])
		context = []
		dates = []

	### GET COURSE

		### With Letter

		result = re.search(r'\w+[ \n]?[ \n]?[ \n]?Science[ \n]?[ \n]?[ \n]?[0-9][0-9][0-9][0-9][a-zA-Z]', text)

		# Check for word + course (i.e. Biology 1000A)
		if result == None:
			result = re.search(r'\w+[ \n]?[ \n]?[ \n]?[0-9][0-9][0-9][0-9][a-zA-Z]', text)

		### Without Letter (BEWARE False-Positives)

		# Check for word + Science + course no letter (i.e. Integrated Science 1000)
		if result == None:
			result = re.search(r'\w+[ \n]?[ \n]?[ \n]?Science[ \n]?[ \n]?[ \n]?[0-9][0-9][0-9][0-9]', text)

		# Check for word + course no letter (i.e. Biology 1000)
		if result == None:
			result = re.search(r'\w+[ \n]?[ \n]?[ \n]?[0-9][0-9][0-9][0-9]', text)

		### Save Results

		if result != None:
			course = result.group()
		else:
			course = "Not Found"

	### GET DATES

		'''YYYY-MM-DD'''
		dates_list = re.findall(r'(\w+)?(?:[ ,:\n]?[ ,:\n]?[ ,:\n]?)(\w+)?(?:[ ,:\n]?[ ,:\n]?[ ,:\n]?)(\d{4}-\d{2}-\d{2})', text)
		for x in dates_list:
			context.append(x[0] + ' ' + x[1])
			dates.append(x[2])
	
		'''Month DD, YYYY'''
		'''Month D, YYYY'''
		'''Month D-D, YYYY'''
		'''Month DD-DD, YYYY'''
		'''Month DD'''
		'''Month D'''
		dates_list = re.findall(r'(\w+)?(?:[ ,:\n]?[ ,:\n]?[ ,:\n]?)(\w+)(?:[ ,:\n]?[ ,:\n]?[ ,:\n]?)(((Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2})(?:–\d{1,2})?(?:,)?(?:\s+(\d{4}))?))', text)
		for x in dates_list:
			context.append(x[0] + ' ' + x[1])
			dates.append(x[2])

		'''MM/DD'''
		'''MM/D'''
		'''M/D'''
		'''M/DD'''
		dates_list = re.findall(r'(\w+)?(?:[ ,:\n]?[ ,:\n]?[ ,:\n]?)(\w+)?(?:[ ,:\n]?[ ,:\n]?[ ,:\n]?)(\d{1,2}\/\d{1,2})', text)
		for x in dates_list:
			context.append(x[0] + ' ' + x[1])
			dates.append(x[2])

		'''MM/DD/YY'''
		'''MM/DD/YYYY'''
		'''DD/MM/YY'''
		'''DD/MM/YYYY'''
		dates_list = re.findall(r'(\w+)?(?:[ ,:\n]?[ ,:\n]?[ ,:\n]?)(\w+)?(?:[ ,:\n]?[ ,:\n]?[ ,:\n]?)(\d{1,2}\/\d{1,2}\/(\d{4}|\d{2}))', text)
		for x in dates_list:
			context.append(x[0] + ' ' + x[1])
			dates.append(x[2])

		'''D-Month'''
		'''DD-Month'''
		'''D Month'''
		'''DD Month'''
		dates_list = re.findall(r'(\w+)?(?:[ ,:\n][ ,:\n][ ,:\n])?(\w+)?(?:[ ,:\n][ ,:\n][ ,:\n])?((\d{1,2})(-|\s)(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?))', text)
		for x in dates_list:
			context.append(x[0] + ' ' + x[1])
			dates.append(x[2])

		for i in range(0, len(dates)):
			date = dates[i]
			con = context[i]
			try:
				parsed = parse(date, fuzzy_with_tokens=True)
				date = parsed[0].strftime('%d-%B-%Y')
			except:
				print("Could not parse date: ", date)
			row = {'File':filename, 'Course':course, 'Deliverable':con, 'Date':date}
			df = df.append(row, ignore_index=True)

		print(dates)
		print("Exit: deadlines_func.py")
		return df



