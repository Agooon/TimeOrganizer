import tkinter as tk
from tkinter import font
from tkinter import *
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
        self.fontSmallest = font.Font(size=9)

        
        self.mainBackground = '#242424'
        self.mainBackgroundDarkerM = '#222'
        self.mainBackgroundDarker = '#111'
        self.mainBackgroundDarkerest = '#000'
        
        self.mainTextColorLighter = '#499'
        self.mainTextColor = '#277'
        self.mainTextColorDarker = '#055'
        self.mainTextColorDarkerest = '#033'

        self.mainBorderLighter = '#555'
        self.mainBorder = '#333'

        self.cursorColor = self.mainTextColor

        self.errorColor = "#900"
        self.successColor = "#0a0"
        

class HeaderBarSetupClass(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        sc = StyleConfigClass()
        self.sc = StyleConfigClass()
        self.master = args[0]
        tk.Toplevel.__init__(self, *args, **kwargs)
        
        self.protocol("WM_DELETE_WINDOW", self.closeWindow)

        self.style = ttk.Style(self.master)
        self.style.theme_use('clam')
        self.attributes('-topmost', 1)

        # Label for title of window
        self.myLabelTitle = tk.Label(self, font = sc.fontBig, background = sc.mainBackgroundDarker, foreground=sc.mainTextColor)
        # Label for default label
        self.myLabel = tk.Label(self, font = sc.fontNormal, 
                                background = sc.mainBackgroundDarker, 
                                foreground=sc.mainTextColor,
                                borderwidth = 1, relief='solid',
                                highlightcolor = sc.mainBorderLighter)
        
        self.myText = tk.Text(self, font=sc.fontSmall, 
                              background =sc.mainBackgroundDarker,
                              insertbackground =  sc.cursorColor,
                              foreground = sc.mainTextColor,
                              padx=5)

        self.style.configure('my.TEntry',padding='5 5 5 5',
                              fieldbackground=sc.mainBackgroundDarker, 
                              background = sc.mainBackgroundDarker,
                              insertbackground =  sc.cursorColor,
                              insertcolor= sc.mainTextColor,
                              foreground = sc.mainTextColor,
                              bordercolor = sc.mainBorderLighter,
                              darkcolor=sc.mainBackgroundDarker, 
                              lightcolor=sc.mainBackgroundDarker) 

        self.myEntry = ttk.Entry(self, style='my.TEntry',font = sc.fontNormal)

        # create custom DateEntry style with red background
        self.style.configure('my.DateEntry', 
                             fieldbackground=sc.mainBackgroundDarker, 
                             foreground = sc.mainTextColor, 
                             background = sc.mainBackgroundDarkerM,
                             arrowcolor = sc.mainTextColor,
                             bordercolor = sc.mainBorderLighter,
                             darkcolor=sc.mainBackgroundDarker, 
                             lightcolor=sc.mainBackgroundDarker,
                             activeforeground = sc.mainTextColor)
        

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

        # Time Entry 
        self.style.configure('myTime.TEntry',
                              padding='5 5 5 5',
                              foreground = sc.mainTextColor, 
                              background = sc.mainBackgroundDarkerM,
                              fieldbackground=sc.mainBackgroundDarker,
                              insertbackground =sc.mainTextColor,
                              bordercolor = sc.mainBorderLighter,
                              darkcolor=sc.mainBackgroundDarker, 
                              lightcolor=sc.mainBackgroundDarker,
                              highlightbackground =sc.mainBackgroundDarker,
                              insertcolor= sc.mainTextColor,
                              selectborderwidth = 0)
        # Hours Entry
        self.vcmdH = (self.register(self.callbackH))
        self.myEntryTimeH = ttk.Entry(self, font = sc.fontNormal, 
                              background = sc.mainBackgroundDarker,
                              foreground = sc.mainTextColor,
                              validate='all', validatecommand=(self.vcmdH, '%P'),
                              justify=RIGHT, style='myTime.TEntry')
        # Minute Entry
        self.vcmdM = (self.register(self.callbackM))
        self.myEntryTimeM = ttk.Entry(self, font = sc.fontNormal, 
                              background = sc.mainBackgroundDarker,
                              foreground = sc.mainTextColor,
                              validate='all', validatecommand=(self.vcmdM, '%P'),
                              justify=LEFT, style='myTime.TEntry')

        # Checkbutton
        self.myCheckB = tk.Checkbutton(self, onvalue=1, offvalue=0, 
                                       font= sc.fontSmall,
                                       foreground = sc.mainTextColor,
                                       background = sc.mainBackgroundDarker,
                                       activebackground = sc.mainTextColor,
                                       borderwidth = 1, relief='solid',
                                       activeforeground = sc.mainBackgroundDarker,
                                       selectcolor = sc.mainTextColorDarkerest)

        # Amount of repeats Entry
        self.vcmdRA = (self.register(self.callbackRA))
        self.myEntryRecurrAmount = ttk.Entry(self, font = sc.fontNormal, 
                              background = sc.mainBackgroundDarker,
                              foreground = sc.mainTextColor,
                              validate='all', validatecommand=(self.vcmdRA, '%P'),
                              justify=LEFT, style='myTime.TEntry',
                              state='disabled')



      
    # To clone the widgets
    def clone(self, widget):
        parent = widget.nametowidget(widget.winfo_parent())
        cls = widget.__class__
        name = cls.__name__

        clone = cls(parent)
        if(name == "DateEntry"):
            keys = self.myDateEntry.keys()
            for key in keys:
                clone.configure({key: widget.cget(key)})
            return clone

        for key in widget.configure():
            if(key !='class'):
                clone.configure({key: widget.cget(key)})
        return clone

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

    #Vaidation of TimePicker 
    # Hours
    def callbackH(self, P):
        if(P == ""):
            return True
   
        if str.isdigit(P) and len(P)<=2:
            val = int(P)
            if val >= 24 or val<0:
                return False
            if(len(P) == 2 and P[0] == "0"):
                return False
            return True
        else:
            return False
    # Minutes
    def callbackM(self, P):
        if(P == ""):
            return True

        if str.isdigit(P) and len(P)<=2:
            val = int(P)
            if val >= 60 or val<0:
                return False
            if(len(P) == 2 and P[0] == "0"):
                return False
            return True
        else:
            return False
    # Minutes
    def callbackRA(self, P):
        if(P == ""):
            return True
        if str.isdigit(P) and len(P)<=2:
            val = int(P)
            if val >= 100 or val<0:
                return False
            if(len(P) == 2 and P[0] == "0"):
                return False
            return True
        else:
            return False
    # Navigatino to other windows
    def openAddEventWindow(self):
        addEventWindowGui(self.master, StyleConfigClass())

    def openMainMenu(self):
        pass

    def openMainMenuAndClose(self):
        pass
    ####### End Header config ############



from TOrganizerFront.AddEventWindow import addEventWindowGui
