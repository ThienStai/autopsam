"""
Autopsam by thien : https://www.github.com/ThienStai/autopsam
A much more powerfull, feature-rich and compact version of MessAttack

"""
from pyautogui import *
#from selenium.webdriver import *
from threading import Thread
from os import *
from ctypes import windll
from pyinputplus import inputInt, inputFloat
from time import  sleep
# making global var
def banner():
    print(""" 
    █████╗ ██╗   ██╗████████╗ ██████╗ ██████╗ ███████╗ █████╗ ███╗   ███╗
    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗████╗ ████║
    ███████║██║   ██║   ██║   ██║   ██║██████╔╝███████╗███████║██╔████╔██║
    ██╔══██║██║   ██║   ██║   ██║   ██║██╔═══╝ ╚════██║██╔══██║██║╚██╔╝██║
    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║     ███████║██║  ██║██║ ╚═╝ ██║
    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                                                                      """)
FAILSAFE = True
SCRWIDTH, SCRHEIGHT = size()

def alert(text="", title=""):
    return windll.user32.MessageBoxW(0, text, title, 0)

def cls():
    banner()
    cls_var = system("cls")
    return cls_var

def countdown(type):
    print(type + " started in 3")
    sleep(1)
    print(type + " started in 2")
    sleep(1)
    print(type + " started in 1")
    sleep(1)
    print("HAVE FUN!")


def main():
    cls()
    global option
    banner()
    while True:
        try:
            option = input("autopsam$")
            if option.lower() == "exit":  # user typed exit
                exit(0)
            if option.lower() == "help":
                # TODO: print the help
                pass
            if option.lower() == "clear" or option.lower() == "cls":
                cls()
            if option.lower() == "autoclick":
                print("Please choose mode:")
                print("1. Lock you mouse on a specific pos to avoid moving")
                print("2. Keep click while you moving the mouse")
                print("0. Go back to main menu")
                option = inputInt("Mode =  ", min=0, max=2)
                if option == 0:
                    pass
                if option == 1: # user choose autoclick + lock
                    print("This will lock you mouse and prevent you from using the mouse")
                    print("Are you sure you want to continue:(y/n)", end=" ")
                    option = input()
                    if option.lower() == "y":
                        XCOR = inputInt("X coor to click = ", min=1, max=SCRWIDTH)
                        YCOR = inputInt("Y coor to click = ", min=1, max=SCRHEIGHT)
                        CLICKTIMES = inputInt("Click amount = ",min=1, max=2147483647 )
                        INTERVAL = inputFloat("Delay between each click = ", min=0.001, max=2147483647)
                        countdown("Autoclick")
                        for i in range(CLICKTIMES):
                            click(x=XCOR, y=YCOR, interval=INTERVAL)
                        alert(text="Done", title="Operation completed!")
                    else:
                        print("You typed \"n\" or invalid option ")
                elif option == 2:
                    CLICKTIMES = inputInt("Click amount = ", min=1, max=2147483647)
                    INTERVAL = inputFloat("Delay between each click = ", min=0.001, max=2147483647)
                    countdown("Autoclick")
                    for i in range(CLICKTIMES):
                        click(interval=INTERVAL)
                    alert(text="Done", title="Operation completed!")
            else:
                print("Invalid command!!!")
                pass
        except (FailSafeException, KeyboardInterrupt):
            alert(text="Operation canceled", title="You cancled the operation")
            cls()
            pass


if __name__ == '__main__':
    main()