from TOrganizerFront.GuiOrganizer import GuiOrganizerClass, StyleConfigClass

from TOrganizerFront.MainWindow import mainWindowGui
import tkinter as tk
from datetime import datetime



def openAddEventWindow():
    guiOrganizer = GuiOrganizerClass()
    sC = StyleConfigClass()
    mainWindowGui(guiOrganizer, sC)
    guiOrganizer.mainloop() 

    


if __name__ == "__main__":
    openAddEventWindow()