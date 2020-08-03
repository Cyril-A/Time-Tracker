This a Python program that allows Nana track the time spent working on his client's project and how much money he made. At the moment, this program does not have external dependencies so it is ready to run

## Installation:
   Before you install, Note that this implementation is in two(2) forms. ie. **Command Line Interaction** and **GUI Interaction**
   
1. To use this program locally, you should have Python 3 installed on your workstation.
2. Under the repository name, click Clone or download
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. Open the terminal and change the current working directory to the location where you want the cloned directory to be made
5. Type git clone, and then paste the URL you copied in Step 3. Press Enter and your local clone will be created.
6. Extract the .py file and **install all dependacies** before running in an editor. 
7. For GUI.py, install the PySimpleGUI module by running ***"pip install pysimplegui"***. It is advisable to run the GUI.py with the **ATOM IDE** by holding the Ctrl + Shift + B buttons to run the script. 

   
  ## PROGRAM DEPENDENCIES
Install the following dependencies. 

`- pandas library`- ***pip install pandas in your terminal*** `pandas` is a software library written for the Python programming language for data manipulation and analysis. It offers data structures and operations for manipulating numerical tables and time series

`- datetime module` ***pip install DateTime*** -supplies classes for manipulating dates and times

`- CSV module`- ***pip install python-csv*** this implements classes to read and write tabular data in CSV format

`- os module`- ***pip install os-sys*** the `OS` module in python provides functions for interacting with the operating system

`- PySimpleGUI library` ***pip install pysimplegui*** - this module allows a graphical interface to the program. 

## How to use:
## *Command Line Interaction.
  1. The user has 2 options:
      - Option1 : Calculate money made in a given time
      - Option2 : To enter a LIVE session
  2. If the user chooses option 1, he inputs the task name. After which he is asked to input the start and end times in the format HH:MM PM/AM. The program then calculates how much time in hours he spent on the project and how much money he earned in dollars at a rate of $5 per hour.
 
  3. If the user decides to go with option 2, he inputs the task name and when he is ready to start work, he types 'start'. The program grabs the exact time and starts timing him untill he types 'stop' when indicates he has finished the task. The program then grabs the exact time at that point and then calculates how much time he spent on that task in hours and how much he earned.
  
  
  ## *Graphical Interaction (GUI)*
  1. Please install the graphical user dependency by typing ***pip install pysimplegui*** in their terminal. 
  With the GUI, the user has the opportunity to perform only one type of task at a time either as *calculating money made in a given time* or *entering a LIVE session*.
  
  2. The GUI can also serve as a **CSV File Viewer.** 
  
  
  # Images From the Software 
  
  ## - Dashboard of Software when launched. 
  ![1](https://user-images.githubusercontent.com/48289239/89139571-9a2be000-d52e-11ea-8e9c-de3ee80730f5.png)
  
  
  ## - Performing a LIVE Session 
  ![2](https://user-images.githubusercontent.com/48289239/89139618-d19a8c80-d52e-11ea-934e-d675f8adbc7b.png)
  
  ## - Calculating Money Earned From a Given Time. 
     Enter both the starting and Ending Time in the format (HH:MM)(AM/PM)
  ![3](https://user-images.githubusercontent.com/48289239/89139625-d8290400-d52e-11ea-828a-c61bfcdddc56.png)
  
  
  ## - Viewing History (CSV File Viewer)
  
      Press the View History Button
  ![4](https://user-images.githubusercontent.com/48289239/89139634-dd864e80-d52e-11ea-98cf-2857985b0b06.png)
  
     Select the CSV File to be Viewed
  ![5](https://user-images.githubusercontent.com/48289239/89139637-de1ee500-d52e-11ea-8338-09a0b3bef7f2.png)
  
     Press OK to View the Files
  ![6](https://user-images.githubusercontent.com/48289239/89139640-e0813f00-d52e-11ea-9119-7d2d7413334d.png)
  
      CSV File Viewer
  ![7](https://user-images.githubusercontent.com/48289239/89141310-c5fd9480-d533-11ea-9499-b259065cebea.png)

  
  
**In both options, the program writes the information, that is, the task, current date, time started and ended to a csv file on his computer for future references**
   
## CONCLUSION:
 
This program meets the client's user requirements.

To get the GUI VERSION 
