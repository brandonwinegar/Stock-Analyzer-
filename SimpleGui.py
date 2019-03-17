from tkinter import *
from tkinter import ttk
import json
import requests
import datetime


class SimpleGui:

    # Build the GUI
    def __init__(self):
        # Creates a Main window and names it 'root'
        root = Tk()
        root.title('my first GUI2')

        # Variables to hold entries and label values
        SimpleGui.symbol = StringVar()
        SimpleGui.result = StringVar()

        # Creates a frame widget, which will hold the all of the content for the UI and attach it to the main window
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)  # Allows the frame to scale with the window if the size is changed
        root.rowconfigure(0, weight=1)  # Allows the frame to scale with the window if the size is changed

        symbol_entry = ttk.Entry(mainframe, width=4, textvariable=self.symbol)
        symbol_entry.grid(column=1, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Get Today's Value", command=self.find_today_val) \
            .grid(column=1, row=3, sticky=W)
        ttk.Label(mainframe, text='Symbol:').grid(column=1, row=1, sticky=(W, E))
        ttk.Label(mainframe, text='default', textvariable=self.result).grid(column=1, row=4, sticky=W)

        symbol_entry.focus()
        root.bind('<Return>', self.find_today_val())

        root.mainloop()

    def find_today_val(self):
        response = self.alphavantage_request('TIME_SERIES_DAILY', self.symbol.get())
        result_json = json.loads(response.text)
        date = self.get_formated_date()
        try:
            today_dict = result_json['Time Series (Daily)'][date]['2. high']
            SimpleGui.result.set(today_dict)
        except KeyError:
            SimpleGui.result.set('KeyError')

    @staticmethod
    def alphavantage_request(func, symbol):
        assembled_url = 'https://www.alphavantage.co/' \
                        'query?function={}&symbol={}&apikey=XW4JRNJTHUYZ8HJC'.format(func, symbol)
        return requests.get(assembled_url)

    @staticmethod
    def get_formated_date():
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)
        day = str(now.day - 1)  #
        # Add leading 0's to match format from alphavantage
        if len(month) < 2: month = '0{}'.format(month)
        if len(day) < 2: day = '0{}'.format(day)
        return '{}-{}-{}'.format(year, month, day)
