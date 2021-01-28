import tkinter as tk
from tkinter import *
from TOrganizerFront.GuiOrganizer import GuiOrganizerClass, StyleConfigClass, HeaderBarSetupClass

#                                           #
#                                           #
############ Global variables ###############
#                                           #
#                                           #
sC = ""

######### Binding variables ###########
eventNameI = ""
eventDescI = ""
eventDateStartI = ""
eventDateEndI = ""

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
#                                           #
#                                           #
############ Front Definition ###############
#                                           #
#                                           #
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)

        self.title("Add new Event")
        self.geometry("480x720")
        self.overrideredirect(True)
        self.configure(background=sC.colorNavyBlue)

        for x in range(8):
            self.grid_columnconfigure(x, weight=1, uniform="fred")
        for y in range(12):
            self.grid_rowconfigure(y, weight=1, uniform="fred")

        #                                     #
        ############ Nav Config ###############
        #                                     #

        self.grip = tk.Label(self, text="Add new event", background = sC.colorViolet, font = sC.fontBig)
        self.grip.grid(column = 0, row = 0, columnspan=8, sticky=W + E + S + N)

        self.grip.bind("<ButtonPress-1>", self.start_move)
        self.grip.bind("<ButtonRelease-1>", self.stop_move)
        self.grip.bind("<B1-Motion>", self.do_move)
        self.grip.bind("<Map>",self.frame_mapped)

        self.exit = tk.Button(self, text=" X ",borderwidth=0, background=sC.colorVioletDark, command= lambda: self.closeApp())
        self.exit.grid(column = 7, row = 0, sticky=E + N)
        self.minimalize = tk.Button(self, text=" - ",borderwidth=0, background=sC.colorVioletDark, command= lambda: self.minimalizeApp())
        self.minimalize.grid(column = 7, row = 0, sticky= N)

        #                                     #
        ############ Rest of Ui ###############
        #                                     #

        self.eventNameLabel = tk.Label(self, text="Event name", font = sC.fontNormal, background = sC.colorViolet, foreground='#f3e25f')
        self.eventNameI = tk.Entry(self, font=sC.fontNormal, background =sC.colorViolet)

        self.eventNameLabel.grid(column = 1, row = 2,columnspan=1, sticky=W + E + S + N)
        self.eventNameI.grid(column = 4, row = 2, columnspan=2, sticky=W + E + S + N)





def addEventWindowGui(guiOrganizer: GuiOrganizerClass, calledSC: StyleConfigClass):
    global sC
    sC = calledSC
    hb = AddEventWindowClass(guiOrganizer)

#def addEventWindowGui(guiOrganizer: GuiOrganizerClass, sC: StyleConfigClass):
#    global eventNameI
#    global eventDescI
#    global eventDateStartI
#    global eventDateEndI
#    global eventFilename
#    global eventFrequency
#    global eventFrequencyRep
    
#    eW = tk.Toplevel(guiOrganizer.master)
#    eW.overrideredirect(True)
#    eW.title("Add new Event")

#    eW.configure(background=sC.colorNavyBlue)
#    eW.geometry("480x720")

#    # 480x720
#    for x in range(8):
#        eW.columnconfigure(x, weight = 0, minsize=50)
#    for y in range(12):
#        eW.rowconfigure(y, weight = 0, minsize=50)

#    # First row
#    eventNameLabel = tk.Label(eW, text="Event name", font = sC.fontNormal,
#    background = sC.colorViolet, foreground='#f3e25f')
#    eventNameI = tk.Entry(eW, font=sC.fontNormal, background =sC.colorViolet)

#    eventNameLabel.grid(column = 1, row = 1,columnspan=2)
#    eventNameI.grid(column = 4, row = 1, columnspan=2)


#    eW.mainloop()




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






