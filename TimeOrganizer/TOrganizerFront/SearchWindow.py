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

class SearchWindowClass(HeaderBarSetupClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.openWindow()
        self.eventL= []

        self.title("Search window")
        self.geometry("650x650")
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
        self.grip['text'] = "Search window"
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

        # 1
        self.searchQueryLabel = self.clone(self.myLabel)
        self.searchQueryLabel['text'] = "Find event: "
        self.searchQueryI = self.clone(self.myText)

        self.searchQueryLabel.grid(column = 0, row = 1,columnspan=3, sticky=W + E + S + N)
        self.searchQueryI.grid(column = 3, row = 1, columnspan=5, sticky=W + E + S + N)

        # 2
        self.dateVar = tk.StringVar()
        self.eventDateStartI = self.clone(self.myDateEntry)
        self.eventDateStartI['date_pattern'] = 'y-mm-dd'
        self.eventDateStartI['textvariable'] = self.dateVar

        self.eventDateStartI.grid(column = 0, row = 2, columnspan=3, sticky=W + E + S + N)

        self.eventDateCheckAF = tk.IntVar()
        self.eventDateCheckAFI = tk.Checkbutton(self, onvalue=1, offvalue=0, 
                                              variable=self.eventDateCheckAF,
                                       font= sc.fontSmall,
                                       foreground = sc.mainTextColor,
                                       background = sc.mainBackgroundDarker,
                                       activebackground = sc.mainTextColor,
                                       borderwidth = 1, relief='solid',
                                       activeforeground = sc.mainBackgroundDarker,
                                       selectcolor = sc.mainTextColorDarkerest)
        self.eventDateCheckAFI['command'] = self.checkAF
        self.eventDateCheckAFI['text'] = 'After'
        self.eventDateCheckAFI.grid(column = 3, row = 2, sticky=W + E + S + N)

        self.eventDateCheckALL = tk.IntVar()
        self.eventDateCheckALLI = tk.Checkbutton(self, onvalue=1, offvalue=0, 
                                              variable=self.eventDateCheckALL,
                                       font= sc.fontSmall,
                                       foreground = sc.mainTextColor,
                                       background = sc.mainBackgroundDarker,
                                       activebackground = sc.mainTextColor,
                                       borderwidth = 1, relief='solid',
                                       activeforeground = sc.mainBackgroundDarker,
                                       selectcolor = sc.mainTextColorDarkerest)
        self.eventDateCheckALLI['command'] = self.checkALL
        self.eventDateCheckALLI['text'] = 'All'
        self.eventDateCheckALLI.grid(column = 4, row = 2,  sticky=W + E + S + N)

        self.eventDateCheckBF = tk.IntVar()
        self.eventDateCheckBFI = tk.Checkbutton(self, onvalue=1, offvalue=0, 
                                              variable=self.eventDateCheckBF,
                                       font= sc.fontSmall,
                                       foreground = sc.mainTextColor,
                                       background = sc.mainBackgroundDarker,
                                       activebackground = sc.mainTextColor,
                                       borderwidth = 1, relief='solid',
                                       activeforeground = sc.mainBackgroundDarker,
                                       selectcolor = sc.mainTextColorDarkerest)
        self.eventDateCheckBFI['command'] = self.checkBF
        self.eventDateCheckBFI['text'] = 'Before'
        self.eventDateCheckBFI.grid(column = 5, row = 2, sticky=W + E + S + N)

        self.searchB = tk.Button(self,font =sc.fontNormal, text="Search Events",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.getEvents())
        self.searchB.grid(column = 6, columnspan=2, row =2, sticky=W + E + S + N)

        # 3 -> 9
        self.listbox = Listbox(self, selectmode=BROWSE, height=10, width=34, exportselection=0, 
                               foreground = sc.mainTextColor, 
                               background=sc.mainBackgroundDarker, 
                               font =('Courier', 10),
                               highlightbackground= sc.mainBackground)
        #self.listbox.item
        self.listbox.grid(column = 0, row = 3, rowspan=9, columnspan=8, sticky=W + E + S + N)


        # 12 and 13
        self.openEventB = tk.Button(self,font =sc.fontBig, text="Open event window",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.openEvent())
        self.openEventB.grid(column = 5, columnspan=3, row =12, rowspan=2, sticky=W + E + S + N)

        self.deleteB = tk.Button(self,font =sc.fontSmall, text="Delete\nevents",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.errorColor, command= lambda: self.deleteChosen())
        self.deleteB.grid(column = 4,  row =12,rowspan=2, sticky=W + E + S + N)


        self.mainMenuWithClose = tk.Button(self,font =sc.fontSmall, text="Menu and close",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.openMainMenuAndClose())
        self.mainMenuWithClose.grid(column = 0, columnspan=4, rowspan=1, row =12, sticky=W + E + S + N)

        self.mainMenuWithClose = tk.Button(self,font =sc.fontSmall, text="Menu and leave",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.openMainMenu())
        self.mainMenuWithClose.grid(column = 0, columnspan=4, rowspan=1, row =13, sticky=W + E + S + N)

        self.initDay()
  
    def initDay(self):
        self.eventDateStartI.set_date(datetime.now())
        self.eventDateCheckALL.set(1)
        self.eventDateCheckBF.set(0)
        self.eventDateCheckAF.set(0)

    def getEvents(self):
        chosenDate = self.dateVar.get()
        #xd =  datetime.strptime(self.dateVar.get(), '%d/%m/%y')
        if(chosenDate != ''):
            self.listbox.delete(0,tk.END)
            dateToGet = date.fromisoformat(chosenDate)
            searchQuery = self.searchQueryI.get("1.0",tk.END)

            if(self.eventDateCheckALL.get() == 1):
                eventList = myBackend.getEvents()
            elif(self.eventDateCheckBF.get() == 1):
                eventList = myBackend.getEventsBefore(dateToGet)
            else:
                eventList = myBackend.getEventsAfter(dateToGet)

            eventList = myBackend.filterNLP(eventList, searchQuery, self.master.searchE)
            self.eventL = eventList
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
                toAdd+=" "+event.dateStart.strftime("%Y-%m-%d")+" | "+event.dateStart.strftime("%H:%M") +" - " + event.dateEnd.strftime("%H:%M") 
                toAdd+="  "
                toAdd+= "|  Name: " + event.name
                self.listbox.insert(tk.END, toAdd)


    def checkALL(self):
        self.eventDateCheckALL.set(1)
        self.eventDateCheckBF.set(0)
        self.eventDateCheckAF.set(0)

    def checkBF(self):
        self.eventDateCheckALL.set(0)
        self.eventDateCheckBF.set(1)
        self.eventDateCheckAF.set(0)

    def checkAF(self):
        self.eventDateCheckALL.set(0)
        self.eventDateCheckBF.set(0)
        self.eventDateCheckAF.set(1)

    def deleteChosen(self):
        self.listbox.delete(0,tk.END)
        myBackend.deleteEventList(self.eventL)
        
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
def searchWindowGui(guiOrganizer: GuiOrganizerClass, calledSC: StyleConfigClass):
    global sc
    sc = calledSC
    hb = SearchWindowClass(guiOrganizer)
