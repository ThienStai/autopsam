"""
Autopsam by thien : https://www.github.com/ThienStai/autopsam
A much more powerfull, feature-rich and compact version of MessAttack

"""
from pyautogui import *
#from selenium.webdriver import *
from threading import Thread
from os import *
# from ctypes import windll
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

def cls():
    cls_var = system("cls")
    banner()
    return cls_var
def cls_nobanner():
    cls_var = system("cls")
    # banner()
    return cls_var


def countdown(type):
    cls_nobanner()
    print(type + " started in 3")
    sleep(1)
    print(type + " started in 2")
    sleep(1)
    print(type + " started in 1")
    sleep(1)
    print("HAVE FUN!")


def main():
    global option
    cls()
    while True:
        cls()
        try:
            option = input("autopsam$ ")
            if option.lower() == "exit":  # user typed exit
                exit(0)
            if option.lower() == "help":  # user typed help
                # TODO: print the help
                print("Loading help file....")
                pass
            if option.lower() == "clear" or option.lower() == "cls": # user want to clrscr
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
            if option.lower() == "box":
                BOXCOUNT = inputInt("Box amount = ", min=1, max=2147483647)
                text = input("Box text = ")
                title = input("Box title = ")
                countdown("Box raid")
                for i in range(BOXCOUNT):
                    t = Thread(target=alert, kwargs={"text": text, "title" : title})
                    t.start()

            else:
                print("Invalid command!!!")
                pass
        except (FailSafeException, KeyboardInterrupt):
            # alert(text="Operation canceled", title="You cancled the operation")
            print("Operation cancled")
            cls_nobanner()
            pass


if __name__ == '__main__':
    main()