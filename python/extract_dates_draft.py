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
		df = pd.DataFrame(columns = ['File', 'Course', 'Deliverable', 'Date'])
		context = []
		dates = []

		result = re.search(r'[a-zA-Z][a-zA-Z][0-9][0-9][0-9][0-9]', text)
		if result == None:
			course = "Not Found"
		else:
			course = result.group()
	
		'''YYYY-MM-DD'''
		dates_list = re.findall(r'(\S+ \S+ )(\d{4}-\d{2}-\d{2})', text)
		for x in dates_list:
			context.append(x[0])
			dates.append(x[1])
	
		'''Month DD, YYYY'''
		'''Month D, YYYY'''
		'''Month D-D, YYYY'''
		'''Month DD-DD, YYYY'''
		'''Month DD'''
		'''Month D'''
		dates_list = re.findall(r'(\S+ \S+ )(((Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2})(?:–\d{1,2})?(?:,)?(?:\s+(\d{4}))?))', text)
		for x in dates_list:
			context.append(x[0])
			dates.append(x[1])

		'''MM/DD'''
		'''MM/D'''
		'''M/D'''
		'''M/DD'''
		dates_list = re.findall(r'(\S+ \S+ )(\d{1,2}\/\d{1,2})', text)
		for x in dates_list:
			context.append(x[0])
			dates.append(x[1])

		'''MM/DD/YY'''
		'''MM/DD/YYYY'''
		'''DD/MM/YY'''
		'''DD/MM/YYYY'''
		dates_list = re.findall(r'(\S+ \S+ )(\d{1,2}\/\d{1,2}\/(\d{4}|\d{2}))', text)
		for x in dates_list:
			context.append(x[0])
			dates.append(x[1])

		'''D-Month'''
		'''DD-Month'''
		'''D Month'''
		'''DD Month'''
		dates_list = re.findall(r'(\S+ \S+ )((\d{1,2})(-|\s)(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?))', text)
		for x in dates_list:
			context.append(x[0])
			dates.append(x[1])

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
		message = df.style.format({c: '<input name="{}" value="{{}}" />'.format(c) for c in df.columns}).render()

		return message



