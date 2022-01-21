# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

from werkzeug.datastructures import FileStorage
import PyPDF2
import tempfile
import docx

class Read():

	def text_pdf(f, directory):
		text = ""
		pdfFileObj = open(directory + f.filename, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		for page_number in range(pdfReader.getNumPages()):
			pageObj = pdfReader.getPage(page_number)
			text += pageObj.extractText()
		return text
					
	def image_pdf(f, directory):
		text = "image-pdf"
		return text
	
	def docx_file(f, directory):										#does not work for tables, headers, footers, foot notes
		text = ""
		doc = docx.Document(directory + f.filename)
		for para in doc.paragraphs:
			text += para.text
		return text
	
	def docx_file(f, directory):
		return text

	def read_func(f):
		print("Enter: read_file.py")
		print(type(f)) 													#FileStorage
		print(f.filename)
		print(f.filename.split('.')[1])
		print(f.content_type)
		text = "Error: unable to read file"
		
		with tempfile.TemporaryDirectory() as directory:
			f.save(directory + f.filename)
			
			if (f.filename.split('.')[1] == "txt"):
				text = f.read().decode("utf-8")
		
			elif (f.filename.split('.')[1] == "docx"): 
				text = Read.docx_file(f, directory)
			
			elif (f.filename.split('.')[1] == "pdf"): 
				text = Read.text_pdf(f, directory) 						#text PDFs
				if (text == ""): text = Read.image_pdf(f, directory) 	#image PDFs
					
		print("Exit: read_file.py")
		return text
		
		
		
		
		

