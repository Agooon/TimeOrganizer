from TOrganizerFront.GuiOrganizer import GuiOrganizerClass, StyleConfigClass
from TOrganizerFront.AddEventWindow import addEventWindowGui
import tkinter as tk



def testing1():
    guiOrganizer = GuiOrganizerClass()
    sC = StyleConfigClass()
   
    addEventWindowGui(guiOrganizer, sC)
    guiOrganizer.mainloop()

    

    


if __name__ == "__main__":
    testing1()