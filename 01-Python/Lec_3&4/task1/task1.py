import pyautogui
import webbrowser
from time import sleep

#Hard Way
'''
# Open the start menu
pyautogui.hotkey('win')
sleep(2)

# Type 'Brave' to search for the browser
pyautogui.write('Brave')
sleep(2)

brave = None
while brave is None :
    try:
        brave = pyautogui.locateOnScreen("task1/brave.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(brave, duration=1)

gmail = None
while gmail is None :
    try:
        gmail = pyautogui.locateOnScreen("task1/gmail.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(gmail, duration=1)


'''

#Easy Way
webbrowser.open("https://mail.google.com/mail/u/1/#inbox")


checkbox = None
while checkbox is None :
    try:
        checkbox = pyautogui.locateOnScreen("task1/checkbox.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(checkbox, duration=1)

MakeAsRead = None
while MakeAsRead is None :
    try:
        MakeAsRead = pyautogui.locateOnScreen("task1/MakeAsRead.png")
    except :
        pyautogui.ImageNotFoundException()
        print("Try again")
pyautogui.click(MakeAsRead, duration=1)
