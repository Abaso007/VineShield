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
import webbrowser
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
        gitimage = gui.CTkImage(light_image=Image.open("git1.png"),dark_image=Image.open("git.png"),size=(30, 30))
        gitbut = gui.CTkButton(master=self.win,text = '',image=gitimage,font=('Arial Rounded MT bold', 18),width = 1,command=self.Git,corner_radius = 8)
        gitbut.place(x=230, y= 5)

        disimage = gui.CTkImage(light_image=Image.open("discord1.png"),dark_image=Image.open("discord.png"),size=(30, 25))
        disbut = gui.CTkButton(master=self.win,text = '',image=disimage,font=('Arial Rounded MT bold', 18),width = 1, height=40,command=self.Discord,corner_radius = 8)
        disbut.place(x=230, y=60)

        self.setTheme = gui.StringVar(value="dark")
        themes = gui.CTkComboBox(master=self.win,values=["dark","light"],variable=self.setTheme,command=self.ThemeChanger,height = 40)
        themes.place(x= 300, y= 5)
    
    def ThemeChanger(self, buf):
        if buf == "dark":
            gui.set_appearance_mode('dark')
            self.win.configure(fg_color="#242424")
        if buf == "light":
            gui.set_appearance_mode('light')
            self.win.configure(fg_color="#EBEBEB")

    def Git(self):
        webbrowser.open('https://github.com/Nick-Vinesmoke', new=2)
    
    def Discord(self):
        webbrowser.open('https://discord.gg/ufvyg5F2j4', new=2)

    def Menu(self) -> None:

        self.win = gui.CTk()

        self.WinConfig()
        self.Widgets()

        frame = gui.CTkFrame(master=self.win, width=260, height=130, fg_color="black", corner_radius= 25)
        frame.place(x=-45, y=-20)
        canvas = gui.CTkCanvas(master=self.win,width=256, height=128, background='white', highlightthickness=0)
        canvas.place(x=0, y=0)
        image = Image.open("logo.png")
        image = image.resize((256, 128))
        image = ImageTk.PhotoImage(image)
        canvas.create_image(128, 64, image=image)

        self.win.mainloop()