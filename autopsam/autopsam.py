"""
Autopsam by thien : https://www.github.com/ThienStai/autopsam
A much more powerfull, feature-rich and compact version of MessAttack

"""
from pyautogui import *
#from selenium.webdriver import *
from os import *
from ctypes import windll
from pyinputplus import inputInt
FAILSAFE = True
def alert(text="", title=""):
    return windll.user32.MessageBoxW(0, text, title, 0)

def cls():
    cls_var = system("cls")
    return cls_var


def main():
    global option
    while True:
        try:
            option = input("autopsam>")
            if option.lower() == "exit":
                exit(0)
            if option.lower() == "help":
                # TODO: print the help
                pass
            if option.lower() == "autoclick":
                print("Please choose mode:")
                print("1. Lock you mouse on a specific pos to avoid moving")
                print("2. Keep click while you moving the mouse")
                option = input("Your option = ")
                if option == "1": # user choose autoclick + lock
                    print("This will lock you mouse and prevent you from using the mouse")
                    print("Are you sure you want to continue:(y/n)", end=" ")
                    option = input()
                    if option.lower() == "y":
                        CLICKTIMES = inputInt("Click amount = ",min=1, max=2147483647 )

                    else:
                        print("You typed \"n\" or invalid option ")


        except (FailSafeException, KeyboardInterrupt):
            alert(text="Operation canceled", title="You cancled the operation")
            pass

if __name__ == '__main__':
    main()