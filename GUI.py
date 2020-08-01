import PySimpleGUI as sg
import time
from datetime import datetime, date, timedelta
import csv

def main():
    theme_dict ={'BACKGROUND': '#2B475D',
                    'TEXT': '#FFFFFF',
                    'INPUT': '#F2EFE8',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#F2EFE8',
                    'BUTTON': ('#000000', '#C2D4D8'),
                    'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                    'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0
                }

    # sg.theme_add_new('Dashboard', theme_dict) 
    sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
    sg.theme('Dashboard')

    BORDER_COLOR = '#C7D5E0'
    DARK_HEADER_COLOR = '#1B2838'
    BPAD_TOP = ((20,20), (20, 10))
    BPAD_LEFT = ((20,10), (0, 10))
    BPAD_LEFT_INSIDE = (0, 20)
    BPAD_RIGHT = ((10,20), (10, 20))

    top_banner = [[sg.Text('Dashboard'+ ' '*64, font='Any 20', background_color=DARK_HEADER_COLOR),
                   sg.Text('Time Tracking Software', font='Any 20', background_color=DARK_HEADER_COLOR)]]

    top  = [[sg.Text('Welcome to the Time Tracking Software', size=(50,1), justification='c', pad=BPAD_TOP, font='Any 20')],
                ]

    block_2 = [[sg.Text('LIVE SESSION',size=(25,1), justification='c', font='Any 20')],
                [sg.Text('Taskname:', font='Any 12'), sg.InputText("", size=(20,10), key='enter'), sg.OK("Enter", font= "Any 12")],
                [sg.Text('Press the Start button to Start: ', font='Any 12'), sg.Button("Start", font="Any 12")],
                [sg.Text('Press the Stop button to stop the Session', font='Any 12'), sg.Button("Stop", font="Any 12")],
                ]

    block_3 = [[sg.Text('Calculate Money Earned From a Given Time', font='Any 15')],
                [sg.Text('Taskname:', font='Any 12'), sg.InputText("", size=(20,10), key='old')],
                [sg.Text('Enter Start Time (HH:MM)(AM/PM):', font='Any 12'), sg.Input(size=(20,10), key="startt")],
                [sg.Text('Enter End time (HH:MM)(AM/PM):', font='Any 12'), sg.Input(size=(20,10), key='endd')],
                [sg.Button('Calculate', font='Any 15')]
                  ]

    block_4 = [
                [sg.Text('Results',size=(40,1), justification='c', font='Any 15')],
                [sg.Multiline(size=(38, 10), font="Any 15", key='ML1')],
                [sg.Button("Clear Results", font="Any 15"), sg.Button("View History", font="Any 15")],

                ]


    layout = [
              [sg.Column(top_banner, size=(960, 60), pad=(0,0), background_color=DARK_HEADER_COLOR)],
              [sg.Column(top, size=(920, 90), pad=BPAD_TOP)],
              [sg.Column([[sg.Column(block_2, size=(450,150), pad=BPAD_LEFT_INSIDE)],
              [sg.Column(block_3, size=(450,170),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR),
               sg.Column(block_4, size=(450, 320), pad=BPAD_RIGHT)]
               ]

    window = sg.Window('Time Tracking', layout, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=False, grab_anywhere=True)
    
    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Enter":
            global taskname
            taskname = values['enter']
        if event == "Start":
            def start_time():
                global start, message, msg
                start = time.time()
                message = time.ctime(int(start))
                msg = f'You started working at {message}'
                return msg
            window['ML1'].update(value = start_time() + '\n')
        if event == "Stop":
            global stop_timer, msg, today
            taskname = values['enter']Z
            today = date.today()
            stop = time.time()
            seconds = stop - start
            hour = round(seconds / 3600, 2)
            PAY_PER_HOUR = 5
            total_money = round((hour * PAY_PER_HOUR), 2)
            stop_timer = time.ctime(int(stop))
            msg1=f'You ended workng at {stop_timer}'
            msg2 = f"Wheeew!!!you have spent {hour} hours..."
            msg3 = f"Nice, you have made ${total_money}..."

            window['ML1'].update(value= msg + '\n' + msg1 +'\n' + '\n' + msg2 + '\n'+'\n' +msg3)


            with open('tracking.csv', 'a', newline="") as csv_file:
                header = ['Type','Current Date', 'Task Name', 'Started', 'Ended ',
                                'Hours', 'Amount Earned $']
                writer = csv.DictWriter(csv_file, fieldnames=header)

                data = {'Type': 'LIVE SESSION', 'Current Date':today, 'Task Name': taskname, 'Started': message,
                                'Ended ': stop_timer, 'Hours': hour,
                                'Amount Earned $': total_money}
                with open('tracking.csv', 'r') as reader:
                    d_reader = csv.DictReader(reader)
                    headers = d_reader.fieldnames
                    if headers == None:
                        writer.writeheader()
                        writer.writerow(data)
                    else:
                        writer.writerow(data)

        if event == "Clear Results":
            window['ML1'].update("")
            window['enter'].update("")

        if event == "View History":
            filename = sg.PopupGetFile('tracking', no_window=False, file_types=(("CSV Files","*.csv"),))
            # --- populate table with file contents --- #
            data = []
            if filename is not None:
                with open(filename, "r") as infile:
                    reader = csv.reader(infile)
                    try:
                        data = list(reader)  # read everything else into a list of rows
                    except:
                        sg.PopupError('Error reading file')
                        exit(69)

            sg.SetOptions(element_padding=(0, 0))

            col_layout = [[sg.Table(values=data, headings=[x for x in range(len(data[0]))], max_col_width=8,
                                    auto_size_columns=False, justification='right', size=(8, len(data)))]]

            layout = [[sg.Column(col_layout, size=(1200,600), scrollable=True)],]

            form = sg.FlexForm('Table', grab_anywhere=False)
            b, v = form.Layout(layout).Read()

        if event == "Calculate":

            global start_minutes, end_minutes, end_mins, end_time
            start_minutes = 0
            end_minutes = 0
            PAY_PER_HOUR = 5
            taskname = values['old']
            start_time = values['startt']
            end_time = values['endd']

            if start_time[-2:] == "PM" and int(start_time[:2 < 12]):
                start_minutes += (int(start_time[:2]) + 12)*60
                start_minutes += (int(start_time[3:5]))

            elif start_time[-2:] == "AM" and int(start_time[:2]) == 12:
                start_minutes += (int(start_time[3:5]))
            else:
                start_minutes += (int(start_time[:2])*60)
                start_minutes += (int(start_time[3:5]))


            if end_time[-2:] == "PM" and int(end_time[:2 < 12]):
                end_minutes += (int(end_time[:2]) + 12)*60
                end_minutes += (int(end_time[3:5]))

            elif end_time[-2:] == "AM" and int(end_time[:2]) == 12:
                end_minutes += (int(end_time[3:5]))
            else:
                end_minutes += (int(end_time[:2])*60)
                end_minutes += (int(end_time[3:5]))

            # converts into the total minutes
            start_mins = start_minutes
            start_hr = start_mins/60
            end_mins = end_minutes  # converts into the total minutes
            end_hr = end_mins/60
            today = date.today()

            if end_mins >= start_mins:  # checs if end_mins >= start_mins
                global mess
                total_mins = end_mins - start_mins  # gets the difference between the two times

                # converts into total hours of work in float
                hour = round((total_mins/60), 2)

                total_money = round((hour * PAY_PER_HOUR), 2)  # finds the total dollars

                n = f'Your Previous task: {taskname}'
                mess = f'Your calculated money is $ {total_money}'

                window['ML1'].update(value= n + '\n' + mess)

                with open('tracking.csv', 'a', newline="") as csv_file:
                    header = ['Type', 'Current Date', 'Task Name', 'Started', 'Ended ',
                                    'Hours', 'Amount Earned $']
                    writer = csv.DictWriter(csv_file, fieldnames=header)

                    data = {'Type': 'OLD WORK', 'Current Date': today, 'Task Name': taskname, 'Started': start_hr,
                                    'Ended ': end_hr, 'Hours': hour,
                                    'Amount Earned $': total_money}
                    with open('tracking.csv', 'r') as reader:
                        d_reader = csv.DictReader(reader)
                        headers = d_reader.fieldnames
                        if headers == None:
                            writer.writeheader()
                            writer.writerow(data)
                        else:
                            writer.writerow(data)
    window.close()

if __name__ == '__main__':
    sg.theme('DarkAmber')
    main()
