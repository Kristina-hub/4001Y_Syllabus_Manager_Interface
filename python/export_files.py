# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #

import pandas as pd

class ExportFiles:

    def output_csv(df):

        csv_path = os.path.abspath(os.path.join(__file__ ,"../..")) + '/output/csv/extract_dates.csv'

        print(df)
        df.to_csv(csv_path, index=False)

        return True

    def output_ics(df):

        ics_path = ''

        print(df)

        # Do .ICS stuff

        return True
