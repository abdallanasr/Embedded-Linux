'''#Threading
import threading
from time import sleep

def task1():
    while True:
        print("Task1 :")
        sleep(1)

def task2():
    while True:
        print("Task2 :")
        sleep(1)

t1 = threading.Thread(target=task1).start()
t2 = threading.Thread(target=task2).start()

while True:
        print("Main Thread :")
        sleep(1)  '''

#GUI
'''
import tkinter as tk

m = tk.Tk()
m.title("GUI")
m.geometry("500x500+500+500")
m.resizable(0,0)
m.mainloop()'''

x = [1,2,3,4,5,6,8,7,9]

x.clear()

print(x)