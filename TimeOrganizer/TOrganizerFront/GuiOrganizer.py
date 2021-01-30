import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

class GuiOrganizerClass(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.openWindows = 0
        self.withdraw()

    def closeWindow(self):
        self.openWindows -= 1
        if(self.openWindows == 0):
            self.destroy()

    def openWindow(self):
        self.openWindows += 1
# To get all styles in 1 place
class StyleConfigClass:
    def __init__(self):
        self.fontBig = font.Font(size=20)
        self.fontNormal = font.Font(size=16)
        self.fontSmall = font.Font(size=12)

        
        self.mainBackground = '#242424'
        self.mainBackgroundDarkerM = '#222'
        self.mainBackgroundDarker = '#111'
        self.mainBackgroundDarkerest = '#000'
        
        self.mainTextColorLighter = '#925fb2'
        self.mainTextColor = '#703ea0'
        self.mainTextColorDarker = '#502c80'
        self.mainTextColorStrong = '#7f00ff'

        self.mainBorderLighter = '#555'
        self.mainBorder = '#333'

        self.cursorColor = '#703ea0'
        

class HeaderBarSetupClass(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        sc = StyleConfigClass()
        self.sc = StyleConfigClass()
        self.master = args[0]
        tk.Toplevel.__init__(self, *args, **kwargs)

        self.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.style = ttk.Style(self.master)
        self.style.theme_use('clam')
        # create custom DateEntry style with red background
        self.style.configure('my.DateEntry', 
                             fieldbackground=sc.mainBackgroundDarker, 
                             foreground = sc.mainTextColor, 
                             background = sc.mainBackgroundDarkerM,
                             arrowcolor = sc.mainTextColor,
                             bordercolor = sc.mainBorderLighter,
                             darkcolor=sc.mainBackgroundDarker, 
                             lightcolor=sc.mainBackgroundDarker)

        self.myLabel = tk.Label(self, font = sc.fontNormal, background = sc.mainBackgroundDarker, foreground=sc.mainTextColor)
        
        self.myText = tk.Text(self, font=sc.fontSmall, 
                              background =sc.mainBackgroundDarker,
                              insertbackground =  sc.cursorColor,
                              foreground = sc.mainTextColor)

        self.myEntry = tk.Entry(self, font = sc.fontNormal, 
                              background = sc.mainBackgroundDarker,
                              insertbackground =  sc.cursorColor,
                              foreground = sc.mainTextColor)

        self.myDateEntry = DateEntry(self, font=sc.fontNormal, style='my.DateEntry',
                                         bordercolor  = sc.mainBorderLighter,
                                         headersbackground = sc.mainBackgroundDarkerM,
                                         headersforeground  = sc.mainTextColor,
                                         foreground = sc.mainTextColor, 
                                         background= sc.mainBackgroundDarker,
                                         normalbackground = sc.mainBackgroundDarker,
                                         normalforeground  = sc.mainTextColor,
                                         weekendbackground  = sc.mainBackgroundDarker,
                                         weekendforeground  = sc.mainTextColor,
                                         othermonthbackground  = sc.mainBackground,
                                         othermonthforeground    = sc.mainTextColor,
                                         othermonthwebackground   = sc.mainBackground,
                                         othermonthweforeground      = sc.mainTextColor)

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

    def openWindow(self):
        print("Opening window: "+ self.__class__.__name__)
        self.master.openWindow()


    def closeWindow(self):
        self.destroy()
        print("Closing window: "+ self.__class__.__name__)
        self.master.closeWindow()


    # Navigatino to other windows
    def openAddEventWindow(self):
        addEventWindowGui(self.master, StyleConfigClass())
    ####### End Header config ############



from TOrganizerFront.AddEventWindow import addEventWindowGui
