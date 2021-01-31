import tkinter as tk
from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from datetime import datetime, timedelta

from TOrganizerFront.GuiOrganizer import GuiOrganizerClass, StyleConfigClass, HeaderBarSetupClass
import TOrganizerFront.Backend as myBackend
import Database.Classes as dbClass
import calendar

eventId = -1
#                                           #
#                                           #
############ Front Definition ###############
#                                           #
#                                           #
class EventWindowClass(HeaderBarSetupClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.openWindow()
        self.event = dbClass.Event()
        self.getValuesFromEvent()
        self.doneUplodaing = False

        self.title("Event window")
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
        self.grip['text'] = "Event window"
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
        self.eventNameI['font'] = sc.fontSmall

        self.eventNameLabel.grid(column = 0, row = 2,columnspan=3, sticky=W + E + S + N)
        self.eventNameI.grid(column = 3, row = 2, columnspan=5, sticky=W + E + S + N)

        # 3 4
        self.eventDescLabel = self.clone(self.myLabel)
        self.eventDescLabel['text'] = "Description: "
        self.eventDescI = self.clone(self.myText)

        self.eventDescLabel.grid(column = 0, row = 3,columnspan=4, rowspan=4, sticky=W + E + S + N)
        self.eventDescI.grid(column = 4, row = 3, columnspan=4,rowspan=4, sticky=W + E + S + N)

        # 5
        self.eventDateStartLabel = self.clone(self.myLabel)
        self.eventDateStartLabel['text'] = "Date start: "
        self.eventDateStartI = self.clone(self.myDateEntry)

        self.eventDateStartLabel.grid(column = 0, row = 7,columnspan=4, sticky=W + E + S + N)
        self.eventDateStartI.grid(column = 4, row = 7, columnspan=4, sticky=W + E + S + N)

        
        # 6
        self.eventTimeStartLabel = self.clone(self.myLabel)
        self.eventTimeStartLabel['text'] = 'Time start:'

        self.eventTimeStartHI = self.clone(self.myEntryTimeH)
        self.eventTimeStartMI = self.clone(self.myEntryTimeM)

        self.eventTimeStartLabel.grid(column = 0, row = 8,columnspan=4,  sticky=W + E + S + N)
        self.eventTimeStartHI.grid(column = 4, row = 8, columnspan=2, sticky=W + E + S + N)
        self.eventTimeStartMI.grid(column = 6, row = 8, columnspan=2, sticky=W + E + S + N)


        # 7
        self.eventTimeEndLabel = self.clone(self.myLabel)
        self.eventTimeEndLabel['text'] = 'Time end:'

        self.eventTimeEndHI = self.clone(self.myEntryTimeH)
        self.eventTimeEndMI = self.clone(self.myEntryTimeM)

        self.evenTimeEndNextDayCheck = tk.IntVar()
        self.evenTimeEndNextDay = self.clone(self.myCheckB)
        self.evenTimeEndNextDay['text'] = 'Next\nDay'
        self.evenTimeEndNextDay['variable'] = self.evenTimeEndNextDayCheck


        self.eventTimeEndLabel.grid(column = 0, row = 9,columnspan=4,  sticky=W + E + S + N)
        self.eventTimeEndHI.grid(column = 4, row = 9, columnspan=2, sticky=W + E + S + N)
        self.eventTimeEndMI.grid(column = 6, row = 9,  sticky=W + E + S + N)
        self.evenTimeEndNextDay.grid(column = 7, row = 9, sticky=W + E + S + N)



        # 12 i 13
        self.changeEventB = tk.Button(self,font =sc.fontBig, text="Save changes",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.updateEvent())
        self.changeEventB.grid(column = 3, columnspan=5, row =11,rowspan=3, sticky=W + E + S + N)

        self.mainMenuWithClose = tk.Button(self,font =sc.fontSmall, text="Menu and close",
                                   background=sc.mainBackgroundDarker, 
                                   foreground=sc.mainTextColor, command= lambda: self.openMainMenuAndClose())
        self.mainMenuWithClose.grid(column = 0, columnspan=3, rowspan=3, row =11, sticky=W + E + S + N)

        self.setUpFields()
  
    def getValuesFromEvent(self):
        e = myBackend.getEvent(eventId)
        if(e == "Error"):
            self.destroy()
        else:
            self.event = e
    def setUpFields(self):
        self.eventNameI.delete(0,tk.END)
        self.eventNameI.insert(0,self.event.name)
        self.eventDescI.delete('1.0',tk.END)
        self.eventDescI.insert(tk.END, self.event.description)
        self.eventNameI.delete(0,tk.END)
        self.eventNameI.insert(0,self.event.name)
        self.eventDateStartI.set_date(self.event.dateStart)
        if(self.event.dateStart.day != self.event.dateEnd.day):
            self.evenTimeEndNextDayCheck.set(1)
        self.eventTimeStartHI.delete(0,tk.END)
        self.eventTimeStartHI.insert(0,self.event.dateStart.hour)
        self.eventTimeStartMI.delete(0,tk.END)
        self.eventTimeStartMI.insert(0,self.event.dateStart.minute)
        self.eventTimeEndHI.delete(0,tk.END)
        self.eventTimeEndHI.insert(0,self.event.dateEnd.hour)
        self.eventTimeEndMI.delete(0,tk.END)
        self.eventTimeEndMI.insert(0,self.event.dateEnd.minute)

        self.doneUplodaing = True


    def updateEvent(self):
         
         if(self.eventNameI.get().replace(" ", "") == ""):
             self.setMessage("Event name can't contain only whitespaces", False)
             return
         if(self.eventDescI.get("1.0",tk.END).replace(" ", "").replace("\n", "") == ""):
             self.setMessage("Description can't contain only whitespaces", False)
             return 
         if(self.eventTimeStartHI.get() == ""):
             self.setMessage("You have to put starting hour", False)
             return 
         if(self.eventTimeEndHI.get() == ""):
             self.setMessage("You have to put ending hour", False)
             return 
         if(self.eventTimeStartMI.get() == ""):
             self.setMessage("You have to put starting minute", False)
             return 
         if(self.eventTimeStartMI.get() == ""):
             self.setMessage("You have to put starting minute", False)
             return 

         startTime = timedelta(hours=int(self.eventTimeStartHI.get()),minutes=int(self.eventTimeStartMI.get()))
         endTime = timedelta(hours=int(self.eventTimeEndHI.get()),minutes=int(self.eventTimeEndMI.get()))
         if(int(self.evenTimeEndNextDayCheck.get()) == 1):
             endTime = endTime + timedelta(days=1)
         else:
             if(startTime >= endTime):
                 self.setMessage("StartTime is larger then EndTime", False)
                 return

                
         dateStart = datetime.strptime(self.eventDateStartI.get_date().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S") + startTime
         dateEnd = datetime.strptime(self.eventDateStartI.get_date().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S") + endTime


         newEvent = dbClass.Event(**{
            'id': eventId,
            'name': self.eventNameI.get(),
            'dateStart': dateStart,
            'dateEnd': dateEnd,
            'description': self.eventDescI.get("1.0",tk.END)})

         msg, succ = myBackend.updateEvent(newEvent,eventId)
         self.setMessage(msg, succ)
         if(succ):
             self.event = newEvent
        

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
def eventWindowGui(guiOrganizer: GuiOrganizerClass, calledSC: StyleConfigClass, id: int):
    global sc
    global eventId
    eventId = id
    sc = calledSC
    hb = EventWindowClass(guiOrganizer)
