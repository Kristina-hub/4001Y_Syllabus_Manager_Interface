# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

import re
from datetime import datetime
from dateutil.parser import parse
from dateparser.search import search_dates
import json
from sutime import SUTime

class Deadlines():
	def deadlines_func(text):
		print("Enter: deadlines_func.py")
		
		sutime = SUTime(mark_time_ranges=True, include_range=True)
		print(json.dumps(sutime.parse(text), sort_keys=True, indent=4))
		
		message = "test"
		print()
		print(text)
		print()
		print(message)
		print()
		print("Exit: deadlines_func.py")
		return message
		
		
		#date = parse(text, fuzzy_with_tokens=True) 				#if year not specified, assume current year
		#message = "{:%B %d, %Y}".format(date[0])
		
		#results = search_dates(text, settings={'STRICT_PARSING':True})							#search_dates tells us what substring is matched to a datetime, we could exclude results matching to “today”
		#for result in results:
		#	print( "{:%B %d, %Y}".format(result[1]) )


		# YYYY-MM-DD
		#matches = re.search(r'\d{4}-\d{2}-\d{2}', text)
		#for match in matches:
		#	datetime_str = datetime.strptime(match.group(), '%Y-%m-%d').date()
		#	format_str = "{:%B %d, %Y}".format(datetime_str)
		#	message += format_str
		#	message += "<br/>"
		
		# MM/D assume current year
		#matches = re.findall(r'\d{2}/\d{1}', text)
		#for match in matches:
		
		# MM/DD assume current year
		# Month D, YYYY
		# Month DD, YYYY
		# Month DD assume year
		# Short forms for months
		
		




		
		

		
		