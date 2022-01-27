# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

import pymysql
import io
from PIL import Image

class ConnectDB():

	def connect_db():
		connection = pymysql.connect(host="34.226.195.49",
					 user="root",
					 passwd="4001Y",
					 db="file_uploads")
		
		'''upload file'''
		connection = sqlite_connect('sample.db')
		cursor = connection.cursor()
		sql_create_table_query = """
		CREATE TABLE audio (name TEXT NOT NULL, data BLOB);
		"""
		cursor.execute(sql_create_table_query)
		connection.commit()
		connection.close()

		'''get file'''
# 		cursor=connection.cursor()
# 		sql1 = 'select * from table'
# 		cursor.execute(sql1)
# 		data2 = cursor.fetchall()
# 		file_like2 = io.BytesIO(data2[0][0])
# 		img1=Image.open(file_like2)
# 		img1.show()
# 		cursor.close()
# 		connection.close()
		
