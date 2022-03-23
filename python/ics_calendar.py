from ics import Calendar, Event
from datetime import datetime
from datetime import timedelta
import pandas as pd

# # ------------------ TEST DATA ----------------------
# test_data = pd.DataFrame(columns=['File', 'Course', 'Deliverable', 'Date'])
# test_data = test_data.append({'File':"BIO_1001A_2021.pdf", 'Course':"B1001A", 'Deliverable':"Test I", 'Date':datetime.strptime("17-10-2022 15:00", "%d-%m-%Y %H:%M")}, ignore_index=True)
# test_data = test_data.append({'File':"CHEM_1301A_2021.pdf", 'Course':"CHEM 1301A", 'Deliverable':"October Quiz", 'Date':datetime.strptime("02-10-2022 10:00", "%d-%m-%Y %H:%M")}, ignore_index=True)
# test_data = test_data.append({'File':"CS_3346A_2021.pdf", 'Course':"CS3346A", 'Deliverable':"Assignment 1", 'Date':datetime.strptime("06-10-2022 23:55", "%d-%m-%Y %H:%M")}, ignore_index=True)
# # ---------------------------------------------------


def upload_event_to_ics_file(df, ics_file_path):
    c = Calendar()

    for event_info in range(df.shape[0]):
        # Formatting the datetime to the correct time zone (+4 hours for London) [time is formatted UTC+0 I think]
        new_date = df['Date'][event_info] + timedelta(hours=4)

        # Setting the event details
        e = Event()
        e.name = df['Deliverable'][event_info] + " - " + df['Course'][event_info]
        e.begin = new_date
        e.end = new_date + timedelta(minutes=5)  # time is formatted UTC+0 (5 hours ahead of the time in London Ontario
        e.description = "Course: " + df['Course'][event_info] + " | " + "Deliverable: " + df['Deliverable'][event_info] + " | " + " Syllabus: " + df['File'][event_info]

        # Adding the event to the calendar
        c.events.add(e)

    # c.events
    with open(ics_file_path, 'w') as my_file:
        my_file.writelines(c)


# upload_event_to_ics_file(test_data, 'events_from_syllabi.ics')
