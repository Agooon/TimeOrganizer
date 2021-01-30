import tkinter as tk
from tkinter import *
from TOrganizerFront.GuiOrganizer import GuiOrganizerClass, StyleConfigClass, HeaderBarSetupClass
from tkcalendar import Calendar, DateEntry
from tkinter import ttk

#                                           #
#                                           #
############ Global variables ###############
#                                           #
#                                           #
sc = ""

######### Binding variables ###########


eventFilename = ""

# everyDay, everyWeek, everyMonth, everyYear
eventFrequency = ""
eventFrequencyRep = ""

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
        self.geometry("480x640")
        self.overrideredirect(True)
        self.configure(background=sc.mainBackground)

        for x in range(8):
            self.grid_columnconfigure(x, weight=1, minsize=60, uniform="fred")
        for y in range(12):
            self.grid_rowconfigure(y, weight=1, minsize=60, uniform="fred")

        #                                     #
        ############ Nav Config ###############
        #                                     #

        self.grip = tk.Label(self, text="Add new event", background = sc.mainBackgroundDarker, font = sc.fontBig)
        self.grip.grid(column = 1, row = 0, columnspan=6, sticky=W + E + S + N)

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
        self.eventNameLabel = self.myLabel
        self.eventNameLabel['text'] = "Event name"
        self.eventNameI = self.myEntry

        self.eventNameLabel.grid(column = 0, row = 2,columnspan=4, sticky=W + E + S + N)
        self.eventNameI.grid(column = 4, row = 2, columnspan=4, sticky=W + E + S + N)

        # 2
        self.eventDescLabel = self.myLabel
        self.eventDescI = self.myText

        self.eventDescLabel.grid(column = 0, row = 3,columnspan=4, rowspan=2, sticky=W + E + S + N)
        self.eventDescI.grid(column = 4, row = 3, columnspan=4,rowspan=2, sticky=W + E + S + N)

        # 3
        self.eventDateStartLabel = tk.Label(self, text="Date start", font = sc.fontNormal, background = sc.mainBackgroundDarker, foreground=sc.mainTextColor)
        self.eventDateStartI = self.myDateEntry

        self.eventDateStartLabel.grid(column = 0, row = 5,columnspan=4, sticky=W + E + S + N)
        self.eventDateStartI.grid(column = 4, row = 5, columnspan=4, sticky=W + E + S + N)

        eventDateStartI = ""
        eventDateEndI = ""





def addEventWindowGui(guiOrganizer: GuiOrganizerClass, calledSC: StyleConfigClass):
    global sc
    sc = calledSC
    hb = AddEventWindowClass(guiOrganizer)



#                                           #
#                                           #
################# Operations ################
#                                           #
#                                           #
def addEvent():
    pass


#                                           #
################# Navigation ################
#                                           #






