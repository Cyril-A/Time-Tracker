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

if choice == 1:

    PAY_PER_HOUR = 5 #amount paid per hour
    task_type = 'Previous Work'
    taskname = input("Enter the Taskname: ")
   
    # function to convert the given time into total minutes
    def minutes_total(time):
        minutes = 0  # stores the minutes to be returned

        # if the entered time is in between 1:00PM and 11:59PM
        if time[-2:] == "PM" and int(time[:2]) < 12:
            minutes += ((int(time[:2])+12)*60)
            minutes += (int(time[3:5]))

        # if entered time is in AM
        elif time[-2:] == "AM" and int(time[:2]) == 12:
            minutes += (int(time[3:5]))

        else:
            minutes += (int(time[:2])*60)
            minutes += (int(time[3:5]))

        return minutes

    while(True):  # accepting input for the start time in the format specified in the print statement.It also checks for a valid time 

        start_time = input("Enter the start time: (hh:mm)(AM/PM)")
        k = start_time  # hh should be in between 0 and 12 and mm should be in between 0 and 59 last two values should be PM or AM and hh should be followed by ':'


        if k[2] == ":" and k[-2:] in ["AM", "PM"] and (int(k[:2]) >= 0 and int(k[:2]) <= 12) and (int(k[3:5]) >= 0 and int(k[3:5]) <= 59):

            break  # if valid then break

            print("Retry!")

    while(True):  # accepting input for the end time in the format specified in the print statement.It also checks for a valid time 
        end_time = input("Enter the end time: (hh:mm)(AM/PM)")
        k = end_time  # hh should be in between 0 and 12 and mm should be in between 0 and 59 last two values should be PM or AM and hh should be followed by ':'

        if k[2] == ":" and k[-2:] in ["AM", "PM"] and (int(k[:2]) >= 0 and int(k[:2]) <= 12) and (int(k[3:5]) >= 0 and int(k[3:5]) <= 59):
            break  # if valid then break
            print("Retry!")

    # using the function created to convert the time into total minutes
    start_mins = minutes_total(start_time)
    end_mins = minutes_total(end_time)  
    today = date.today() #getting the current date

    while end_mins >= start_mins:  # checks while end_mins >= start_mins
        total_mins = end_mins - start_mins  #difference between the two times and storing the value in total_mins

        # converts into total hours of work in float
        hour = round((total_mins/60), 2)

        total_money = hour * PAY_PER_HOUR  # finds the total money
        
        print(f"Wheeew!!!you have spent {hour} hours...")#prints the number of hours worked
        print(f"Nice! you have made ${round(total_money,2)}")  #prints amount of money made
        
        createCSV()
        addToCSV(task_type, today, taskname, start_time, end_time, hour, round(total_money,2) )

        break
    else:
        print("End time is less that Start time of the day")

        
# Entering the LIVE Project mode
elif choice == 2:

    PAY_PER_HOUR = 5  #amount paid per hour
    task_type = 'LIVE Session'

    taskname = input("Enter the name of the task: ")

    inputt = input("Type 'start' to start timer...")
    
    #makes sure nana types 'start' to start the timer
    while (inputt != 'start'): 
        inputt = input("Oops, let's try again! Type 'start' to start timer...\n")

    start = time.time()
    print(f'You started workng at {time.ctime(int(start))}')

    inputt = input("Type 'stop' to stop timer...")

    while (inputt != 'stop'): #makes sure Nana types 'stop' to stop the timer
        inputt = input("Type stop to stop timer...\n")

    stop = time.time()
    print(f'You ended workng at {time.ctime(int(stop))}')

    seconds = stop - start
    start_time = time.ctime(int(start))
    end_time = time.ctime(int(stop))
    today = date.today() #getting the current date
    
    hour = round(seconds / 3600, 3) #converting the seconds to hours
    total_money = hour * PAY_PER_HOUR #calculating amount of money made
    
    createCSV()
    addToCSV(task_type, today, taskname, start_time, end_time, hour, round(total_money,2))

    print(f"Wheeew!!!you have spent {hour} hours...") #prints the number of hours worked
    print(f"Nice! you have made ${round(total_money,2)}...") #prints amount of money made
             
      
