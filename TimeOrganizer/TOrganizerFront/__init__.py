from TOrganizerFront.GuiOrganizer import GuiOrganizerClass, StyleConfigClass
from TOrganizerFront.AddEventWindow import addEventWindowGui
from TOrganizerFront.EventWindow import eventWindowGui
import tkinter as tk



def openAddEventWindow():
    guiOrganizer = GuiOrganizerClass()
    sC = StyleConfigClass()
    eventWindowGui(guiOrganizer, sC, 5)
    guiOrganizer.mainloop() 

    


if __name__ == "__main__":
    openAddEventWindow()