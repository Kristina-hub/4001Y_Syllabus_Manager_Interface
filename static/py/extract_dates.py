# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

# from dateparser.search import search_dates

class Deadlines():
	def deadlines_func(text):
		print("Enter: deadlines_func.py")
		
# 		http://theautomatic.net/2018/12/18/2-packages-for-extracting-dates-from-a-string-of-text-in-python/
# 		https://stackoverflow.com/questions/14279058/parse-multiple-dates-using-dateutil
# 		message = ""
# 		results = search_dates(text, settings={'STRICT_PARSING':True})							#search_dates tells us what substring is matched to a datetime, we could exclude results matching to “today”
# 		for result in results:
# 			print( "{:%B %d, %Y}".format(result[1]) )
# 			message += "{:%B %d, %Y}".format(result[1])
# 			message += "<br/>"


		match_str = re.search(r'\d{4}-\d{2}-\d{2}', text)
		res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()
		message = str(res)

		print()
		print(text)
		print()
		print(message)
		print()
		print("Exit: deadlines_func.py")
		return message

