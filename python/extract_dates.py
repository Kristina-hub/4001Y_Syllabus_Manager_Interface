# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

import os
import re
import pandas as pd
		
class ExtractDates():

	def dates_func(text, filename):
		print("Enter: deadlines_func.py")
		#csv_path = os.path.abspath(os.path.join(__file__ ,"../..")) + '/output/csv/extract_dates.csv'
		csv_path = os.path.abspath(os.path.join(__file__ ,"../..")) + '/output/extract_dates.csv'
		
		'''Type: Assignment/Test/Project/Final/Midterm'''
		df = pd.DataFrame(columns = ['File', 'Course', 'Deliverable', 'Date', 'Type'])  
		dates = []
	
		'''YYYY-MM-DD'''
		dates += re.findall(r'\d{4}-\d{2}-\d{2}', text)
	
		'''Month DD, YYYY'''
		'''Month D, YYYY'''
		'''Month D-D, YYYY'''
		'''Month DD-DD, YYYY'''
		'''Month DD'''
		'''Month D'''
		dates_list = re.findall(r'((Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t)?(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2})(?:–\d{1,2})?(?:,)?(?:\s+(\d{4}))?)', text)
		[dates.append(x[0]) for x in dates_list]

		'''MM/DD'''
		'''MM/D'''
		'''M/D'''
		'''M/DD'''
		dates += re.findall(r'\d{1,2}\/\d{1,2}', text)

		'''MM/DD/YY'''
		'''MM/DD/YYYY'''
		'''DD/MM/YY'''
		'''DD/MM/YYYY'''
		dates += re.findall(r'\d{1,2}\/\d{1,2}\/(\d{4}|\d{2})', text)

		for date in dates:
			row = {'File':filename, 'Course':'null', 'Deliverable':'null', 'Date':date, 'Type':'null'}
			df = df.append(row, ignore_index=True)

		print(df)
		df.to_csv(csv_path, index=False)
		
		print(dates)
		print("Exit: deadlines_func.py")
		message = df.to_html()
		return message



