import tkinter as tk
from tkinter import *
from TOrganizerFront.GuiOrganizer import GuiOrganizerClass, StyleConfigClass, HeaderBarSetupClass
from tkcalendar import Calendar, DateEntry
from tkinter import ttk

import TOrganizerFront.Backend as myBackend
import Database.Classes as dbClass
import calendar
#                                           #
#                                           #
############ Front Definition ###############
#                                           #
#                                           #
class AddEventWindowClass(HeaderBarSetupClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.openWindow()

        self.title("Add new Event")
        self.geometry("480x650")
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
        self.grip['text'] = "Add New Event"
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

        # 1 Message to UI
        self.infoLine = self.clone(self.myText)
        self.infoLine['background'] = sc.mainBackgroundDarkerM
        self.infoLine['state'] = 'disabled'
        self.infoLine['font'] = sc.fontSmall
        self.infoLine.grid(column = 0, row = 1, columnspan=8, sticky=W + E + S + N)

        # 2
        self.eventNameLabel = self.clone(self.myLabel)
        self.eventNameLabel['text'] = "Event name: "
        self.eventNameI = self.clone(self.myEntry)

        self.eventNameLabel.grid(column = 0, row = 2,columnspan=4, sticky=W + E + S + N)
        self.eventNameI.grid(column = 4, row = 2, columnspan=4, sticky=W + E + S + N)

        # 3 4
        self.eventDescLabel = self.clone(self.myLabel)
        self.eventDescLabel['text'] = "Description: "
        self.eventDescI = self.clone(self.myText)

        self.eventDescLabel.grid(column = 0, row = 3,columnspan=4, rowspan=2, sticky=W + E + S + N)
        self.eventDescI.grid(column = 4, row = 3, columnspan=4,rowspan=2, sticky=W + E + S + N)

        # 5
        self.eventDateStartLabel = self.clone(self.myLabel)
        self.eventDateStartLabel['text'] = "Date start: "
        self.eventDateStartI = self.clone(self.myDateEntry)
        self.eventDateStartI['date_pattern'] = 'y-mm-dd'

        self.eventDateStartLabel.grid(column = 0, row = 5,columnspan=4, sticky=W + E + S + N)
        self.eventDateStartI.grid(column = 4, row = 5, columnspan=4, sticky=W + E + S + N)

        
        # 6
        self.eventTimeStartLabel = self.clone(self.myLabel)
        self.eventTimeStartLabel['text'] = 'Time start:'

        self.eventTimeStartHI = self.clone(self.myEntryTimeH)
        self.eventTimeStartMI = self.clone(self.myEntryTimeM)

        self.eventTimeStartLabel.grid(column = 0, row = 6,columnspan=4,  sticky=W + E + S + N)
        self.eventTimeStartHI.grid(column = 4, row = 6, columnspan=2, sticky=W + E + S + N)
        self.eventTimeStartMI.grid(column = 6, row = 6, columnspan=2, sticky=W + E + S + N)


        # 7
        self.eventTimeEndLabel = self.clone(self.myLabel)
        self.eventTimeEndLabel['text'] = 'Time end:'

        self.eventTimeEndHI = self.clone(self.myEntryTimeH)
        self.eventTimeEndMI = self.clone(self.myEntryTimeM)

        self.evenTimeEndNextDayCheck = tk.IntVar()
        self.evenTimeEndNextDay = self.clone(self.myCheckB)
        self.evenTimeEndNextDay['text'] = 'Next\nDay'
        self.evenTimeEndNextDay['variable'] = self.evenTimeEndNextDayCheck


        self.eventTimeEndLabel.grid(column = 0, row = 7,columnspan=4,  sticky=W + E + S + N)
        self.eventTimeEndHI.grid(column = 4, row = 7, columnspan=2, sticky=W + E + S + N)
        self.eventTimeEndMI.grid(column = 6, row = 7,  sticky=W + E + S + N)
        self.evenTimeEndNextDay.grid(column = 7, row = 7, sticky=W + E + S + N)

        # 8
        self.eventRecurrCheck = tk.IntVar()
        self.eventTimeRecurr = tk.Checkbutton(self, onvalue=1, offvalue=0, 
                                              variable=self.eventRecurrCheck,
                                       font= sc.fontSmall,
                                       foreground = sc.mainTextColor,
                                       background = sc.mainBackgroundDarker,
                                       activebackground = sc.mainTextColor,
                                       borderwidth = 1, relief='solid',
                                       activeforeground = sc.mainBackgroundDarker,
                                       selectcolor = sc.mainTextColorDarkerest)
        self.eventTimeRecurr['command'] = self.isRecurring
        self.eventTimeRecurr['text'] = 'Is repeating'
        self.eventTimeRecurr.grid(column = 0, row = 8, columnspan=8, sticky=W + E + S + N)

        # 9
        self.menuRecurrVal = tk.Variable()
        self.eventRecurrOptions = tk.OptionMenu(self,self.menuRecurrVal, 
                                                "Every day","Every week", "Every month", "Every Year")
        self.menuRecurrVal.set("Every day")
        self.eventRecurrOptions.config(activebackground = sc.mainBackgroundDarkerM,
                              activeforeground = sc.mainTextColor,
                              font = sc.fontNormal,
                              background = sc.mainBackgroundDarker,
                              foreground = sc.mainTextColor,
                              highlightbackground = sc.mainBackgroundDarker,
                              highlightthickness=0,
                              state = 'disabled')
        self.eventRecurrOptions["menu"].configure(font = sc.fontNormal,
                                                  activeborderwidth = 0,
                                                  relief= "flat",
                                                  bg=  sc.mainBackgroundDarker,
                                                  borderwidth = 55,
                                                  fg =sc.mainTextColor,
                                                  activebackground = sc.mainBackgroundDarkerM,
                                                  activeforeground = sc.mainTextColor)

        self.eventRecurrOptions.grid(column = 0, row = 9, columnspan=3, sticky=W + E + S + N)

        self.eventRecurrAmountLabel = self.clone(self.myLabel)
        self.eventRecurrAmountLabel['text'] = 'Repeats(max 99):'
        self.eventRecurrAmountLabel['font'] = sc.fontSmall
        self.eventRecurrAmountLabel['state'] = 'disabled'

        self.eventRecurrAmountI = self.clone(self.myEntryRecurrAmount)
        self.eventRecurrAmountLabel.grid(column = 3, row = 9,columnspan=3,  sticky=W + E + S + N)
        self.eventRecurrAmountI.grid(column = 6, row = 9, columnspan=2, sticky=W + E + S + N)

        # 11

        self.eventAddFromFileLabel = self.clone(self.myLabel)
        self.eventAddFromFileLabel['text'] = 'File name:'

        self.eventAddFromFileI = self.clone(self.myEntry)

        self.eventAddFromFileButton = tk.Button(self,font =sc.fontSmallest, text="Add Events\nfrom file",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.addEventFromFile())


        self.eventAddFromFileLabel.grid(column = 0, row = 11,columnspan=2, sticky=W + E + S + N)
        self.eventAddFromFileI.grid(column = 2, row = 11, columnspan=4, sticky=W + E + S + N)
        self.eventAddFromFileButton.grid(column = 6, row =11,columnspan=2, sticky=W + E + S + N)

        # 12 i 13
        self.addEventB = tk.Button(self,font =sc.fontNormal, text="Add Event",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.addEventButton())
        self.addEventB.grid(column = 3, columnspan=5, row =12,rowspan=2, sticky=W + E + S + N)

        self.mainMenuWithClose = tk.Button(self,font =sc.fontSmall, text="Menu and close",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.openMainMenuAndClose())
        self.mainMenuWithClose.grid(column = 0, columnspan=3, row =12, sticky=W + E + S + N)

        self.mainMenuWithoutClose = tk.Button(self,font =sc.fontSmall, text="Menu and leave", 
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.openMainMenu())
        self.mainMenuWithoutClose.grid(column = 0, columnspan=3, row = 13, sticky=W + E + S + N)

        


    def isRecurring(self):
        if(self.eventRecurrCheck.get() == 1):
            self.eventRecurrOptions['state'] = 'normal'
            self.eventRecurrAmountI['state'] = 'normal'
            self.eventRecurrAmountLabel['state'] = 'normal'
        else:
            self.eventRecurrOptions['state'] = 'disabled'
            self.eventRecurrAmountI['state'] = 'disabled'
            self.eventRecurrAmountLabel['state'] = 'disabled'

    def addEventButton(self):
        msg, succ = myBackend.addEventButton(
            str(self.eventNameI.get()),      str(self.eventDescI.get("1.0",tk.END)), 
            self.eventDateStartI.get_date(), str(self.eventTimeStartHI.get()),  
            str(self.eventTimeEndHI.get()),  str(self.eventTimeStartMI.get()), 
            str(self.eventTimeEndMI.get()),  str(self.evenTimeEndNextDayCheck.get()), 
            str(self.eventRecurrCheck.get()),     str(self.eventRecurrAmountI.get()), 
            str(self.menuRecurrVal.get()))
        self.setMessage(msg,succ)
   

    def addEventFromFile(self):
        fileName = str(self.eventAddFromFileI.get())
        msg,succ=myBackend.addEventsFromFile(fileName)
        self.setMessage(msg,succ)
        

    def setMessage(self,msg:str, success:bool):
        self.infoLine['state'] = 'normal'
        self.infoLine.delete('1.0',tk.END)
        if(success):
            self.infoLine['foreground'] = sc.successColor
        else:
            self.infoLine['foreground'] = sc.errorColor
        self.infoLine.insert(tk.END,msg)
        self.infoLine['state'] = 'disabled'


#                                           #
############## Initialization ###############
#                                           #

def addEventWindowGui(guiOrganizer: GuiOrganizerClass, calledSC: StyleConfigClass):
    global sc
    sc = calledSC
    hb = AddEventWindowClass(guiOrganizer)
