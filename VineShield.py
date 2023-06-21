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
        file = str(input(style.CYAN))
        print(style.BLUE+"[?]name of build",end="")
        print(style.VIOLET+">>> ",end="")
        name = str(input(style.CYAN))
        print(style.BLUE+"[?]path to icon or none",end="")
        print(style.VIOLET+">>> ",end="")
        icon = str(input(style.CYAN))
        input(style.YELLOW+"[i]press enter to start")

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