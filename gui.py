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
from PIL import ImageTk, Image
#from ctypes import windll, byref, sizeof, c_int
#import os

class GUI:
    def __init__(self) -> None:
        self.Menu()

    def WinConfig(self) -> None:
        self.win.geometry("500x600+560+240")  
        self.win.minsize(500,400)
        self.win.title("VineShield") 
        self.win.resizable(False, False)  
        self.win.configure(fg_color="#242424")
        self.win.iconbitmap('icon.ico')  
        gui.set_appearance_mode('dark')
        gui.set_default_color_theme('transparent-theme.json')
        #self.HWND = windll.user32.GetParent(self.win.winfo_id())
        #barCol = 0x000000FF
        #windll.dwmapi.DwmSetWindowAttribute(self.HWND, 35, byref(c_int(barCol)), sizeof(c_int))
    
    def Widgets(self):
        pass
    def Menu(self) -> None:

        self.win = gui.CTk()

        self.WinConfig()
        self.Widgets()
        canvas = gui.CTkCanvas(master=self.win,width=256, height=128, background='white', highlightthickness=0)
        image = Image.open("logo.png")
        image = image.resize((256, 128))
        image = ImageTk.PhotoImage(image)
        canvas.create_image(128, 64, image=image)
        canvas.place(relx=0.5, rely=0.18, anchor=CENTER)


        self.win.mainloop()