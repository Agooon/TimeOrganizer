import tkinter as tk
from tkinter import font


class GuiOrganizerClass(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()

# To get all styles in 1 place
class StyleConfigClass:
    def __init__(self):
        self.fontBig= font.Font(size=20)
        self.fontNormal = font.Font(size=16)
        self.fontSmall = font.Font(size=12)
        self.colorViolet = '#813ea0'
        self.colorVioletLightDark = '#703ea0'
        self.colorVioletDark = '#502c80'
        self.colorGold = '#f3e25f'
        self.colorNavyBlue = '#082f5a'

class HeaderBarSetupClass(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        self.master = args[0]
        tk.Toplevel.__init__(self, *args, **kwargs)

    #                                    #
    ########### Header config ############
    #                                    #
    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def frame_mapped(self,e):
        self.update_idletasks()
        self.overrideredirect(True)
        self.state('normal')

    def minimalizeApp(self):
        self.overrideredirect(False)
        self.state('iconic')

    def closeApp(self):
        self.master.destroy()
    ####### End Header config ############




