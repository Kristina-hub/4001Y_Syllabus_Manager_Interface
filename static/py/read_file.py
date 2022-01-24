# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

class Read():

	def read_func(fileToLoad):
		f = open(fileToLoad, "r")
		textFromFile = f.read()
		print("Print read_file.py to terminal - textFromFile: " + textFromFile)
		returnText = "Print read_file.py to website - textFromFile: " + textFromFile
		return returnText

