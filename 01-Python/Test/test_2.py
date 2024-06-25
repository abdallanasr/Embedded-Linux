#pass
'''
while True :
    pass
'''

#loop
i = 0
while i < 10:
    print(i, end=" ")
    i += 1

print("\n")

for i in range(10):
    if i % 2 == 0:
        print(i, end= " ")
    i+=1 

print("\n")

for i in range(10):
    print(i, end= " ")
else:
    print("\nLoop finished.")

#shorthand for
[print(i, end= " ") for i in range(5) if i%2 == 0]

print("\n")

#Useful scripts


#DateTime
import datetime

print(datetime.datetime.now())

import pyfiglet

print(pyfiglet.figlet_format("Abdalla"))


#Built in function

Name = "Abdalla"
print(len(Name))

#Object functions

x = "abdalla Nasr Farag "

print(x.split(" "))

age = 22
name = "abdalla"

print("name %s  age %d"%(name,age))
print("name {}  age {}".format(name,age))
print("name {}  age {}".format(name,age))
print ("name {0}  age {1}".format(name,age ))
print(f"name {name}  age {age}")

#Functions
#Normal Void
def Print():
    print("Hello")

Print()

#Normal Return
def Sum(x,y):
    print(f"x + y = {x+y}")

Sum(25,16)

#Value Assign
def my_fun(child1,child2,child3):
    print("Child1 is : " + child1)
    print("Child2 is : " + child2)
    print("Child3 is : " + child3)

my_fun(child3="Abdalla",child2="Nasr",child1="Ali")

#Value Default
def summ(x = 2, y = 3):
    print(f"x + y = {x+y}")

summ()
summ(5,15)

#Variadic Argument Tuple (*)
def fun(*arg):
    print(type(arg))
    print(arg[0])
    print(arg[1])
    print(arg[2])

fun(1,2,3)

#Variadic Argument Dic (**)
def funn(**arg):
    print(arg["name"])
    print(arg["age"])
    print(arg["email"])

funn(name = "abdalla", age = 15, email = "**************************")

thisdic = {
    "name" : "Abdalla",
    "age" : 15,
    "email" : "*********************",
}
funn(**thisdic)


def examble(name, *degree):
    print("My name is "+ name)
    print("This is my degrees")
    for i in degree:
        print(f"{i}",end=" ")
    print("\n")

examble("Abdalla",(25,30,19,25,18,22,3))

x = (5,9,8,6,33,5,47,8,2,45,9)

examble("Hossam",x)


#Lambda function

x = lambda a : a+10
print(x(5))

x = lambda a , b , c : (a + b) * c
print(x(15,2,6))

#module
import requests
from pprint import pprint
'''url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

pprint(url.json())'''

#Quic Task
#Largest Element

x = [55,2,4,88,9,6,77,3]
print(x)
x.sort()
print(f"Largest element is {x[-1]}")

print(f"Largest element is {max(x)}")

#Modules
import module

module.sum(5,10) 

from module import div as d

d(10,2)

#another module
import platform

print(platform.system())
print(platform.processor())
print(platform.python_compiler())
print(platform.release())
print(platform.node())

#another module
import importlib

print(importlib.import_module('pyfiglet'))
print(importlib.import_module('requests'))

#List Methods

lis = [1,2,3,4,5,6,7,8,"Abdalla"]
#Shallow Copy
lis.append("Nasr")
p = lis
p.append("7")

print(p)
print(lis)

#Deep Copy

c = lis.copy()

c.append(55)
print(c)
print(lis)

#Task
import Firefox
'''
Firefox.Firefox(Firefox.facebook)
Firefox.Firefox(Firefox.x)
Firefox.Firefox(Firefox.instagram) 
Firefox.Firefox(Firefox.youtube)'''

#Set
print("************************************************")
g = {'a','b','c','d','s'}

g.add('aas')
print(g)
g.add('ewww')
print(g)
g.update('ssss','dddddd')
print(g)

#pyautogui
import pyautogui
from time import sleep
'''sleep(2)
location = None
while location is None:
    location = pyautogui.locateOnScreen('image.png')
    sleep(1)

pyautogui.click(location)'''

pyautogui.hotkey('win')
pyautogui.write('termin')
sleep(2)
location = None
while location is None:
    location = pyautogui.locateOnScreen('image copy 2.png')
    sleep(1)
pyautogui.click(location,duration=1)
sleep(2)
pyautogui.write('sudo apt upgrade')
pyautogui.hotkey('enter')
sleep(1)
pyautogui.write('2510')
pyautogui.hotkey('enter')