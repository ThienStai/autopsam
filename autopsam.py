"""
Autopsam by thien : https://www.github.com/ThienStai/autopsam
A much more powerfull, feature-rich and compact version of MessAttack

"""
from pyautogui import *
from selenium.webdriver import Edge, Chrome
from selenium.webdriver.common.keys import Keys
from threading import Thread
from pyinputplus import *
from time import sleep
from os import *


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


def messthread(username="", password="", target="", logged_in=True, time=int(), enter_delay=float(), string=""):
    global browser
    browser = drivergen()
    if logged_in:
        browser.get(url=("https://www.messenger.com/t/" + target))
    else:
        browser.get(url="https://www.messenger.com/login")
        username_input_box = browser.find_element_by_id("email")
        username_input_box.send_keys(username)
        password_input_box = browser.find_element_by_id("pass")
        password_input_box.send_keys(password)
        browser.find_element_by_tag_name("html").send_keys(Keys.ENTER)
        sleep(5)
        browser.get(url=("https://www.messenger.com/t/" + target))
    sleep(5)
    textbox = browser.find_element_by_id("placeholder-8njeg")
    for i in range(time):
        textbox.send_keys(string)
        sleep(enter_delay)
        textbox.send_keys(Keys.ENTER)

def drivergen():
    # --------------------------------------handle the driver-----------------------------------------------#
    print("\n\nDownload the driver and put it in the same folder with this file")
    print("Detecting drivers in current folder: " + os.getcwd() + "...")
    if not ChromeDriverExist() and MsEdgeDriverExist():
        print("Found Edge driver")
        br_option = input("Are you want to continue?\n>")
        if br_option.lower() == "y" or br_option.lower() == "yes":
            return Edge(executable_path=".\\msedgedriver.exe")
        else:
            PATH = inputFilepath("Full path to driver = ", blank=False, mustExist=True)
            return Edge(executable_path=PATH)
    elif not MsEdgeDriverExist() and ChromeDriverExist():
        print("Found Chrome driver")
        br_option = input("Are you want to continue?\n>")
        if br_option.lower() == "y" or br_option.lower() == "yes":
            return Chrome(executable_path=".\\chromedriver.exe")
        else:
            print("Please enter full path for Chrome driver")
            PATH = inputFilepath("Full path to driver = ", blank=False, mustExist=True)
            return Chrome(executable_path=PATH)
    elif MsEdgeDriverExist() and ChromeDriverExist():
        print("Found both edge and chrome driver, choose which?\n")
        print("E  -------  Edge")
        print("C  -------  Chrome")
        br_option = input("\nI choose ")
        if br_option.lower() == "c" or br_option.lower() == "chrome":
            print("Set to chrome")
            return Chrome(executable_path=".\\chromedriver.exe")
        else:
            print("Set to edge")
            return Edge(executable_path=".\\msedgedriver.exe")
    else:
        print("Unable to locate the driver...")
        print("Choose the broser type?\n")
        print("E  -------  Edge")
        print("C  -------  Chrome")
        br_option = input("\nI choose ")
        if br_option.lower() == "c" or br_option.lower() == "chrome":
            PATH = inputFilepath("Full path to driver = ", blank=False, mustExist=True)
            return Chrome(executable_path=PATH)
        else:
            PATH = input("FULL PATH to edge driver = ")
            return Edge(executable_path=PATH)

    # --------------------------------------------------------------------------------------------------------#


def ChromeDriverExist():
    if os.path.isfile(os.path.join(os.getcwd(), "chromedriver.exe")):
        return True
    else:
        return False


def MsEdgeDriverExist():
    if os.path.isfile(os.path.join(os.getcwd(), "msedgedriver.exe")):
        return True
    else:
        return False


def cls():
    cls_var = system("cls")
    banner()
    return cls_var


def cls_nobanner():
    cls_var = system("cls")
    return cls_var


def countdown(type):
    cls_nobanner()
    for i in range(3):
        print(type + "start after %s " % (3 - i))
        sleep(1)
    print("Have fun")


def main():
    cls()
    global FAILSAFE, option, browser, USERNAME, PASSWORD,THREADCOUNT,target,letter_delay,string,time_thread, enter_delay
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
            if option.lower() == "clear" or option.lower() == "cls":  # user want to clrscr
                cls()
            if option.lower() == "autoclick":
                print("Please choose mode:")
                print("1. Lock you mouse on a specific pos to avoid moving")
                print("2. Keep click while you moving the mouse")
                print("0. Go back to main menu")
                option = inputInt("Mode =  ", min=0, max=2)
                if option == 0:
                    pass
                if option == 1:  # user choose autoclick + lock
                    print("This will lock you mouse and prevent you from using the mouse")
                    print("Are you sure you want to continue:(y/n)", end=" ")
                    option = input()
                    if option.lower() == "y":
                        XCOR = inputInt("X coor to click = ", min=1, max=SCRWIDTH)
                        YCOR = inputInt("Y coor to click = ", min=1, max=SCRHEIGHT)
                        CLICKTIMES = inputInt("Click amount = ", min=1, max=2147483647)
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
            if str(option).lower() == "box":
                BOXCOUNT = inputInt("Box amount = ", min=1, max=2147483647)
                text = input("Box text = ")
                title = input("Box title = ")
                countdown("Box raid")
                for i in range(BOXCOUNT):
                    t = Thread(target=alert, kwargs={"text": text, "title": title})
                    t.start()
                alert(text="Done", title="Operation completed!")


            elif option.lower() == "mess":
                print("\nChoose a attack:\n")
                print("unsafe : type as fast as possible, may cause lag")
                print("safe   : type with delay and fail-safe")
                option = input("\nYour option: ").lower()
                if option.lower() == "unsafe":
                    print("\nIf lag then move your mouse to any screen corner to exit!")
                    FAILSAFE = True
                    string_to_spam = input("String to spam = ")
                    times = inputInt("Time to spam = ", min=1, max=2147483647)
                    countdown(type="Mess Atack")
                    for i in range(0, times):
                        typewrite(string_to_spam)
                        press('enter')
                        print("Spammed %s times, %s spams left" % (i, times - i))
                    alert(text="Done", title="Operation completed!")

                elif option.lower() == "exit":
                    exit(0)

                elif option.lower() == "safe":
                    print("\nIf lag then move your mouse to any screen corner to exit!\n")
                    FAILSAFE = True
                    string_to_spam = input("String to spam = ")
                    times_to_spam = inputInt("Time to spam = ", min=1, max=2147483647)
                    enter_delay = inputFloat("Delay between typing string and press enter = ", min=0.002,
                                             max=2147483647)
                    letter_delay = inputFloat("Delay between each letters = ", min=0.002, max=2147483647)
                    countdown(type="Mess Attack")
                    for i in range(0, times_to_spam):
                        typewrite(string_to_spam, interval=letter_delay)
                        sleep(enter_delay)
                        press('enter')
                        print("Spammed %s times, %s spams left" % (i, times_to_spam - i))
                    alert(text="Done", title="Operation completed!")
                    sleep(1)
            elif option.lower() == "mess_mul_thread":
                target = input("Target username/id = ")
                letter_delay = inputFloat("Delay between each letters = ", min=0.001, max=2147483647)
                string = input("String you want to spam = ")
                enter_delay = inputFloat("Delay between typing string and press enter = ", min=0.002,max=2147483647)
                time_thread = inputInt("Time to spam for each thread = ", min=1, max=2147483647)
                USERNAME = input("Your username/id/email = ")
                PASSWORD = inputPassword("You password = ", mask="*")
                print("For each thread, this will spawn a new browser window and spam ")
                THREADCOUNT = inputInt("Thread count = ", min=1, max=2147483647)
                for i in range(THREADCOUNT):
                    t = Thread(target=messthread, kwargs={"username"    : USERNAME,
                                                          "password"    : PASSWORD,
                                                          "target"      : target,
                                                          "string"      : string,
                                                          "logged_in"   : True,
                                                          "time"        : time_thread,
                                                          "enter_delay" : enter_delay
                                                          })
                    t.start()

                alert(text="Done", title="Operation completed!")
            else:
                print("Invalid command!!!")
                pass
        except (FailSafeException, KeyboardInterrupt):
            alert(text="Operation canceled", title="You cancled the operation")
            cls_nobanner()
            pass


if __name__ == '__main__':
    main()
