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
from tkinter import filedialog
#from ctypes import windll, byref, sizeof, c_int
#import os

class GUI:
    def __init__(self, theme = 'themes/theme.json', mode = 'dark') -> None:
        self.theme = theme
        if self.theme == 'themes/theme.json':
            self.varTheme = 'transparent'
        else:
            self.varTheme = 'colored'
        self.mode = mode
        self.Menu()

    def WinConfig(self) -> None:
        self.win.geometry("500x600+560+240")  
        self.win.minsize(500,400)
        self.win.title("VineShield") 
        self.win.resizable(False, False)  
        self.win.iconbitmap('icon.ico')  
        gui.set_appearance_mode(self.mode)
        gui.set_default_color_theme(self.theme)
        if self.mode == 'dark':
            self.win.configure(fg_color="#242424")
        if self.mode == 'light':
            self.win.configure(fg_color="#F2F2F2")

        #self.HWND = windll.user32.GetParent(self.win.winfo_id())
        #barCol = 0x000000FF
        #windll.dwmapi.DwmSetWindowAttribute(self.HWND, 35, byref(c_int(barCol)), sizeof(c_int))
    
    def Widgets(self):
        gitimage = gui.CTkImage(light_image=Image.open("img_files/git1.png"),dark_image=Image.open("img_files/git.png"),size=(30, 30))
        gitbut = gui.CTkButton(master=self.win,text = '',image=gitimage,font=('Arial Rounded MT bold', 18),width = 1,command=self.Git,corner_radius = 8)
        gitbut.place(x=230, y= 5)

        disimage = gui.CTkImage(light_image=Image.open("img_files/discord1.png"),dark_image=Image.open("img_files/discord.png"),size=(30, 25))
        disbut = gui.CTkButton(master=self.win,text = '',image=disimage,font=('Arial Rounded MT bold', 18),width = 1, height=40,command=self.Discord,corner_radius = 8)
        disbut.place(x=230, y=60)

        self.setMode = gui.StringVar(value=self.mode)
        mode = gui.CTkComboBox(master=self.win,values=["dark","light"],variable=self.setMode,command=self.ModeChanger,height = 40)
        mode.place(x= 300, y= 5)

        self.setTheme = gui.StringVar(value=self.varTheme)
        themes = gui.CTkComboBox(master=self.win,values=["transparent","colored"],variable=self.setTheme,command=self.ThemeChanger,height = 40)
        themes.place(x= 300, y= 60)

        main = gui.CTkFrame(master=self.win, width=260, height=130, corner_radius= 25, border_width=2)
        main.place(x= 0, y= 120)

        header1 = gui.CTkLabel(master=self.win, text = "Main", font=('Arial Rounded MT bold', 24),bg_color= ['#E5E5E5','#212121'])
        header1.place(x= 13, y= 125)

        self.fileVar = gui.StringVar(value="select file")
        fileSelecter = gui.CTkButton(master=self.win, textvariable=self.fileVar,font=('Arial Rounded MT bold', 18), corner_radius = 8, bg_color= ['#E5E5E5','#212121'], command= self.SelectFile)
        fileSelecter.place(x= 100, y= 130)

        self.iconVar = gui.StringVar(value="select icon")
        iconSelecter = gui.CTkButton(master=self.win, textvariable=self.iconVar,font=('Arial Rounded MT bold', 18), corner_radius = 8, bg_color= ['#E5E5E5','#212121'], command= self.SelectIcon)
        iconSelecter.place(x= 100, y= 170)

        fileName = gui.CTkEntry(master=self.win,font=('Arial Rounded MT bold', 14), bg_color= ['#E5E5E5','#212121'], placeholder_text= 'output file name')
        fileName.place(x= 100, y= 210)

    def SelectFile(self):
        self.file = filedialog.askopenfilename(title="select file.exe",defaultextension=".exe",filetypes=[("executable files",".exe")])
        if self.file != '':
            index = self.file.rfind('/')
            text = self.file[index+1:]
            if len(text) < 15:
                self.fileVar.set(text)
            else:
                text = text[:11]
                text+= '...'
                self.fileVar.set(text)
        else:
            self.fileVar.set("not selected")
    
    def SelectIcon(self):
        self.icon = filedialog.askopenfilename(title="select file.ico",defaultextension=".ico",filetypes=[("icon files",".ico")])
        if self.icon != '':
            index = self.icon.rfind('/')
            text = self.icon[index+1:]
            if len(text) < 15:
                self.iconVar.set(text)
            else:
                text = text[:11]
                text+= '...'
                self.iconVar.set(text)
        else:
            self.iconVar.set("not selected")

    def ThemeChanger(self,buf):
        if buf == "transparent":
            self.win.destroy()
            GUI('themes/theme.json', self.setMode.get())
        if buf == "colored":
            self.win.destroy()
            GUI('themes/theme1.json',self.setMode.get())
    
    def ModeChanger(self, buf):
        if buf == "dark":
            self.win.destroy()
            GUI(self.theme, "dark")
        if buf == "light":
            self.win.destroy()
            GUI(self.theme, "light")

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
        image = Image.open("img_files/logo.png")
        image = image.resize((256, 128))
        image = ImageTk.PhotoImage(image)
        canvas.create_image(128, 64, image=image)

        self.win.mainloop()