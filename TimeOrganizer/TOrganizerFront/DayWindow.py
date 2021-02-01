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

class DayWindowClass(HeaderBarSetupClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.openWindow()
        

        self.title("Day window")
        self.geometry("650x650")
        self.overrideredirect(True)
        self.configure(background=sc.mainBackgroundDarkerM)

        for x in range(8):
            self.grid_columnconfigure(x, weight=1, minsize=60, uniform="fred")
        for y in range(14):
            self.grid_rowconfigure(y, weight=1, minsize=45, uniform="fred")
        self.grid_rowconfigure(10, weight=1, minsize=30, uniform="fred")
        self.grid_rowconfigure(1, weight=1, minsize=65, uniform="fred")
        #                                     #
        ############ Nav Config ###############
        #                                     #

        self.grip = self.clone(self.myLabelTitle)
        self.grip['text'] = "Day window"
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


        # 1 -> 10
        self.dateVar = tk.StringVar()
        self.dateVar.trace_add('write', lambda name, index, mode: self.checkDate())

        self.eventDateStartLabel = self.clone(self.myLabel)
        self.eventDateStartLabel['text'] = "Select Date: "
        self.eventDateStartI = self.clone(self.myDateEntry)
        self.eventDateStartI['date_pattern'] = 'y-mm-dd'
        self.eventDateStartI['textvariable'] = self.dateVar

        self.eventDateStartLabel.grid(column = 0, row = 1,columnspan=4, sticky=W + E + S + N)
        self.eventDateStartI.grid(column = 4, row = 1, columnspan=4, sticky=W + E + S + N)

        

        self.listbox = Listbox(self, selectmode=BROWSE, height=10, width=34, exportselection=0, 
                               foreground = sc.mainTextColor, 
                               background=sc.mainBackgroundDarker, 
                               font =('Courier', 12),
                               highlightbackground= sc.mainBackground)
        #self.listbox.item
        self.listbox.grid(column = 0, row = 2, rowspan=10, columnspan=8, sticky=W + E + S + N)


        # 12 and 13
        self.changeEventB = tk.Button(self,font =sc.fontBig, text="Open event window",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.openEvent())
        self.changeEventB.grid(column = 3, columnspan=5, row =12,rowspan=2, sticky=W + E + S + N)

        self.mainMenuWithClose = tk.Button(self,font =sc.fontSmall, text="Menu and close",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.openMainMenuAndClose())
        self.mainMenuWithClose.grid(column = 0, columnspan=3, rowspan=2, row =12, sticky=W + E + S + N)

        self.initDay()
  
    def initDay(self):
        self.eventDateStartI.set_date(date)
    def checkDate(self):
        chosenDate = self.dateVar.get()
        if(chosenDate != ''):
            self.listbox.delete(0,tk.END)
            dateToGet = date.fromisoformat(chosenDate)
            eventList = myBackend.getEventsFromDay(dateToGet)
            longestid = 1
            
            for event in eventList:
                newid = len(str(event.id))
                if(newid>longestid):
                    longestid=newid
            for event in eventList:
                
                toAdd = str(event.id)+". "
                if(len(toAdd)-2<longestid):
                    for i in range(longestid-len(toAdd)+2):
                        toAdd+=" "
                toAdd+="| "+event.dateStart.strftime("%H:%M") +" - " + event.dateEnd.strftime("%H:%M") 
                if(event.dateStart.day != dateToGet.day):
                    toAdd+= " B "
                elif(event.dateEnd.day != dateToGet.day):
                    toAdd+= " A "
                else:
                    toAdd+="   "
                toAdd+= "|  Name: " + event.name
                self.listbox.insert(tk.END, toAdd)

    def openEvent(self):
        try:
            indexToGo:str = self.listbox.get(self.listbox.curselection())
        except:
            indexToGo:str = "NIE_WYBRANO!"
            return
        indexToGo = indexToGo.partition(".")[0]
        self.openEventWindow(int(indexToGo))

#                                           #
############## Initialization ###############
#                                           #
def dayWindowGui(guiOrganizer: GuiOrganizerClass, calledSC: StyleConfigClass, passedDate:datetime):
    global sc
    global date
    date = passedDate
    sc = calledSC
    hb = DayWindowClass(guiOrganizer)

