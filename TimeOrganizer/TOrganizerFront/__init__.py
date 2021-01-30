from TOrganizerFront.GuiOrganizer import GuiOrganizerClass, StyleConfigClass
from TOrganizerFront.AddEventWindow import addEventWindowGui
import tkinter as tk



def openAddEventWindow():
    guiOrganizer = GuiOrganizerClass()
    sC = StyleConfigClass()
    addEventWindowGui(guiOrganizer, sC)
    guiOrganizer.mainloop() 

    


if __name__ == "__main__":
    openAddEventWindow()