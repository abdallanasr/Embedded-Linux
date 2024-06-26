import pyautogui
from time import sleep

def install_release():
    install_release = None
    while install_release is None:
        try:
            install_release = pyautogui.locateOnScreen("install_release.png")
        except :
            pyautogui.ImageNotFoundException()
            print("Try again")
    pyautogui.click(install_release, duration=1)

def install() :
    install = None
    install_release = None
    uninstall = None
    while install is None and uninstall is None and install_release is None:
        try:
            try:
                #install_release = pyautogui.locateOnScreen("install_release.png")
                install = pyautogui.locateOnScreen("install.png")
                flag = 0
            except:
                uninstall = pyautogui.locateOnScreen("uninstall.png")
                flag = 1
        except :
        
            pyautogui.ImageNotFoundException()
            print("Try again")
    if flag == 1:
        pass
    elif flag == 0:
        pyautogui.click(install, duration=1)

#Open vscode
pyautogui.hotkey("win")
sleep(1)
pyautogui.write("vscode")

vscode = None
while vscode is None:
    try:
        vscode = pyautogui.locateOnScreen("vscode.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(vscode, duration=1)

#Open extensions
extension = None
extension1 = None
while extension is None and extension1 is None:
    try:
        try:
            extension = pyautogui.locateOnScreen("extension.png")
            flag = 0
        except:
            extension1 = pyautogui.locateOnScreen("extension1.png")
            flag = 1
    except :
        
        pyautogui.ImageNotFoundException()
        print("Try again")

if flag == 1:
    pyautogui.click(extension1, duration=1)
    pyautogui.click(extension1, duration=1)
elif flag == 0:
    pyautogui.click(extension, duration=1)

#Delete text and search on clangd
sleep(3)
pyautogui.hotkey("ctrl", "a", "delete")
pyautogui.write("clangd")

clangd = None
while clangd is None :
    try:
        clangd = pyautogui.locateOnScreen("clangd.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(clangd, duration=1)

install() 

#Delete text and search on c++ testmate
clear = None
while clear is None :
    try:
        clear = pyautogui.locateOnScreen("clear.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(clear, duration=1)

pyautogui.write("c++ testmate")
sleep(3)
pyautogui.click(300, 200, duration=1)

install() 

#Delete text and search on c++ helper
clear = None
while clear is None :
    try:
        clear = pyautogui.locateOnScreen("clear.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(clear, duration=1)

pyautogui.write("c++ helper")
sleep(3)
pyautogui.click(300, 200, duration=1)

install()

#Delete text and search on cmake  
clear = None
while clear is None :
    try:
        clear = pyautogui.locateOnScreen("clear.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(clear, duration=1)

pyautogui.write("cmake ")
sleep(3)
pyautogui.click(300, 200, duration=1)

install() 

#Delete text and search on cmake tools
clear = None
while clear is None :
    try:
        clear = pyautogui.locateOnScreen("clear.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(clear, duration=1)

pyautogui.write("cmake tools")
sleep(3)
pyautogui.click(300, 200, duration=1)

install_release() 
