import pandas as pd
from datetime import datetime

df = pd.DataFrame(columns=['File', 'Course', 'Deliverable', 'Date'])
df = df.append({'File':"BIO_1001A_2021.pdf", 'Course':"B1001A", 'Deliverable':"Test I", 'Date':datetime.strptime("17-10-2022 15:00", "%d-%m-%Y %H:%M")}, ignore_index=True)
df = df.append({'File':"CHEM_1301A_2021.pdf", 'Course':"CHEM 1301A", 'Deliverable':"October Quiz", 'Date':datetime.strptime("02-10-2022 10:00", "%d-%m-%Y %H:%M")}, ignore_index=True)
df = df.append({'File':"CS_3346A_2021.pdf", 'Course':"CS3346A", 'Deliverable':"Assignment 1", 'Date':datetime.strptime("06-10-2022 23:55", "%d-%m-%Y %H:%M")}, ignore_index=True)

print(df)
