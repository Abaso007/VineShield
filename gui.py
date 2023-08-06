'''
 __      __ _                _____  _      _        _      _ 
 \ \    / /(_)              / ____|| |    (_)      | |    | |
  \ \  / /  _  _ __    ___ | (___  | |__   _   ___ | |  __| |
   \ \/ /  | || '_ \  / _ \ \___ \ | '_ \ | | / _ \| | / _` |
    \  /   | || | | ||  __/ ____) || | | || ||  __/| || (_| |
     \/    |_||_| |_| \___||_____/ |_| |_||_| \___||_| \__,_| 
                 
by Nick-Vinesmoke
github: https://github.com/Nick-Vinesmoke
original: https://github.com/Nick-Vinesmoke/VineShield
'''

from tkinter import *
import customtkinter as gui

class GUI:
    def __init__(self) -> None:
        self.Menu()

    def WinConfig(self) -> None:
        #self.win.overrideredirect(1)
        self.win.geometry("500x600+560+240")  
        self.win.minsize(500,400)
        self.win.title("VineShield") 
        self.win.resizable(False, False)  
        self.win.configure(fg_color="#242424")
        self.win.iconbitmap('icon.ico')  
        gui.set_appearance_mode('dark')
        gui.set_default_color_theme('transparent-theme.json')

    def Menu(self) -> None:

        self.win = gui.CTk()

        self.WinConfig()

        self.win.mainloop()