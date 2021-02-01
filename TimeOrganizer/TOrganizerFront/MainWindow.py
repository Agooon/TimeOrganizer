import tkinter as tk
from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from datetime import datetime, timedelta,date

from TOrganizerFront.GuiOrganizer import GuiOrganizerClass, StyleConfigClass, HeaderBarSetupClass
import TOrganizerFront.Backend as myBackend
import Database.Classes as dbClass
import calendar

#                                           #
#                                           #
############ Front Definition ###############
#                                           #
#                                           #

class MainWindowClass(HeaderBarSetupClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.openWindow()
        

        self.title("Main window")
        self.geometry("750x650")
        self.overrideredirect(True)
        self.configure(background=sc.mainBackgroundDarkerM)

        for x in range(8):
            self.grid_columnconfigure(x, weight=1, minsize=60, uniform="fred")
        for y in range(14):
            self.grid_rowconfigure(y, weight=1, minsize=45, uniform="fred")
        #                                     #
        ############ Nav Config ###############
        #                                     #

        self.grip = self.clone(self.myLabelTitle)
        self.grip['text'] = "Main window"
        self.grip.grid(column = 0, row = 0, columnspan=8, sticky=W + E + S + N)

        self.grip.bind("<ButtonPress-1>", self.start_move)
        self.grip.bind("<ButtonRelease-1>", self.stop_move)
        self.grip.bind("<B1-Motion>", self.do_move)
        self.grip.bind("<Map>",self.frame_mapped)

        self.exit = tk.Button(self, text="  X  ",borderwidth=0, background=sc.mainBackgroundDarker, foreground=sc.mainTextColor, command= lambda: self.closeWindow())
        self.exit.grid(column = 7, row = 0, sticky=E + N)
        self.minimalize = tk.Button(self, text="  - ",borderwidth=0, background=sc.mainBackgroundDarker, foreground=sc.mainTextColor, command= lambda: self.minimalizeApp())
        self.minimalize.grid(column = 7, row = 0, sticky= N)

        #                                     #
        ############ Rest of Ui ###############
        #                                     #
        self.dateVar = tk.StringVar()
        self.calendar = Calendar(self, font=sc.fontNormal, style='my.DateEntry',
                                         bordercolor  = sc.mainBorderLighter,
                                         headersbackground = sc.mainBackgroundDarkerM,
                                         headersforeground  = sc.mainTextColor,
                                         foreground = sc.mainTextColor, 
                                         background= sc.mainBackgroundDarker,
                                         normalbackground = sc.mainBackgroundDarker,
                                         normalforeground  = sc.mainTextColor,
                                         weekendbackground  = sc.mainBackgroundDarker,
                                         weekendforeground  = sc.mainTextColor,
                                         othermonthbackground  = sc.mainBackground,
                                         othermonthforeground    = sc.mainTextColor,
                                         othermonthwebackground   = sc.mainBackground,
                                         othermonthweforeground      = sc.mainTextColor)
        
       
        self.calendar.grid(column = 0, row = 1, rowspan=10, columnspan=8, sticky= N + S +W +E)
        self.calendar['date_pattern'] = 'y-mm-dd'
        self.calendar['textvariable'] = self.dateVar

        # Navigation Buttons
        

        self.addEventB = tk.Button(self, text="Add Event Window",borderwidth=0, 
                                   font = sc.fontNormal,
                                   background=sc.mainBackgroundDarker, foreground=sc.mainTextColor, command= lambda: self.openAddEventWindow())
        self.addEventB.grid(column = 0,columnspan=2, row = 11,rowspan=2, sticky= N + S +W +E)

        self.searchB = tk.Button(self, text="Search Event Window",borderwidth=0, 
                                   font = sc.fontNormal,
                                   background=sc.mainBackgroundDarker, foreground=sc.mainTextColor, command= lambda: self.openSearchWindow())
        self.searchB.grid(column = 3,columnspan=2, row = 11,rowspan=2, sticky= N + S +W +E)

        self.dayWindowB = tk.Button(self, text="Day Window",borderwidth=0, 
                                    font = sc.fontNormal,
                                    background=sc.mainBackgroundDarker, foreground=sc.mainTextColor, command= lambda: self.goToDay())
        self.dayWindowB.grid(column = 6, columnspan=2, row = 11, rowspan=2, sticky= N + S +W +E)


        # Bottom label

        self.footer = self.clone(self.myLabel)
        self.footer['text'] = 'Time organizer by Adam Sierakowski'
        self.footer['foreground'] = sc.mainTextColorDarker
        self.footer.grid(column = 0, row = 13, columnspan=8, sticky= N + S +W +E)
  
    def goToDay(self):
        chosenDate = self.dateVar.get()
        if(chosenDate != ''):
            dateToGet = date.fromisoformat(chosenDate)
            self.openDayWindow(dateToGet)
        x=1


#                                           #
############## Initialization ###############
#                                           #
def mainWindowGui(guiOrganizer: GuiOrganizerClass, calledSC: StyleConfigClass):
    global sc
    sc = calledSC
    hb = MainWindowClass(guiOrganizer)
