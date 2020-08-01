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
