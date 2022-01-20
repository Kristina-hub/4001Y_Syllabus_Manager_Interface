# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

from werkzeug.datastructures import FileStorage

class Read():

	def read_func(f):
		print(type(f))
		text = f.read().decode("utf-8")
		print("Print read_file.py to terminal - textFromFile: " + text)
		returnText = "Print read_file.py to website - textFromFile: " + text
		return returnText

