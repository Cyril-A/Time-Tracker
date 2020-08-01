import time
from datetime import datetime, date, timedelta
import csv
import pandas as pd
import os


print("*****************************************************")
print("\tWelcome Time Tracking Program")
print("*****************************************************")
print("Enter the number to select an option:")
print("Press [1] to calculate money made in a given time")
print("Press [2] to enter a LIVE session")

choice = int(input("Enter your Option: "))

# create file.csv
def createCSV():
    # check if file.csv exists already
    if os.path.exists('./tracking.csv'):
        return
    # creates file.csv with columns only
    else:
        columns = pd.DataFrame(columns=['Type', 'Current Date', 'Task name', 'Started', 'Ended', 'hours','Amount earned $'])
        # save file.csv
        columns.to_csv('./tracking.csv')
        return
    
#function to add the data to the file   
def addToCSV(task_type, today, taskname, start_time, end_time, hour, total_money):
    csv_list = ['',task_type, today, taskname, start_time, end_time, hour, total_money]
    my_file = open('./tracking.csv', 'a')
    writer = csv.writer(my_file, delimiter=',')
    writer.writerow(csv_list)
    my_file.flush()
    my_file.close()
    return 1


             
