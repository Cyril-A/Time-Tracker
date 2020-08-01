This a Python program that allows Nana track the time spent working on his client's project and how much money he made. At the moment, this program does not have external dependencies so it is ready to run

## Installation:

1. To use this program locally, you should have Python 3 installed on your workstation.
2. Under the repository name, click Clone or download
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. Open the terminal and change the current working directory to the location where you want the cloned directory to be made
5. Type git clone, and then paste the URL you copied in Step 3. Press Enter and your local clone will be created.
3. Extract the .py file and run in an editor.

   
  ## PROGRAM DEPENDENCIES

`- pandas library`- `pandas` is a software library written for the Python programming language for data manipulation and analysis. It offers data structures and operations for manipulating numerical tables and time series

`- datetime module` -supplies classes for manipulating dates and times

`- CSV module`- this implements classes to read and write tabular data in CSV format

`- os module`-the `OS` module in python provides functions for interacting with the operating system

## How to use:
  1. The user has 2 options:
      - Option1 : Calculate money made in a given time
      - Option2 : To enter a LIVE session
  2. If the user chooses option 1, he inputs the task name. After which he is asked to input the start and end times in the format HH:MM PM/AM. The program then calculates how much time in hours he spent on the project and how much money he earned in dollars at a rate of $5 per hour.
 
  3. If the user decides to go with option 2, he inputs the task name and when he is ready to start work, he types 'start'. The program grabs the exact time and starts timing him untill he types 'stop' when indicates he has finished the task. The program then grabs the exact time at that point and then calculates how much time he spent on that task in hours and how much he earned.
   
**In both options, the program writes the information, that is, the task, current date, time started and ended to a csv file on his computer for future references**
   
## CONCLUSION:
 
This program meets the client's user requirements.
