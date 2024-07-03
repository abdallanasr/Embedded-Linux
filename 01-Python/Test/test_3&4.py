#Dictionary
'''
thisdic1 = {
    "Name" : "Abdalla",
    "Age" : 22,
    "Country" : "Egypt",
    "FAculty" : "Engineering"  
}

thisdic2 = dict([
    ("Name" , "Abdalla"),
    ("Age" , 22),
    ("Country" , "Egypt"),
    ("FAculty" , "Engineering)")
])

thisdic3 = dict(
    Name = "Abdalla",
    Age = 22,
    Country = "Egypt",
    FAculty = "Engineering"
)

print(thisdic1)
print(thisdic2)
print(thisdic3)

for x , y in thisdic1.items():
    print(f"{x} : {y}")
print("\n***************************************")

#Funtions
#Pass by value

def funVar(x):
    x = 55
    print("Inside : ", x)
    print("Inside : ", id(x))

x = 10
print("Before Function : ", x)
print("Before Function : ", id(x))

funVar(x)
print("After Function : ", x)
print("After Function : ", id(x))

print("\n***************************************")
#Pass by reference

def funLis(x):
    x[0] = 55
    print("Inside : ", x)
    print("Inside : ", id(x))

x = [10]
print("Before Function : ", x)
print("Before Function : ", id(x))

funLis(x)
print("After Function : ", x)
print("After Function : ", id(x))

print("\n***************************************")


#Datetime Module
import datetime

time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time)

#math Module
#Has a lot of useful functions
import math


#Object Oriented Programming

class Person:
    name = ""

    def __init__(self, name):
        print("Constructor has been created")
        print(name)
        print(f"Address of **{name}** is {self}")

    def __del__(self):
        print("Constructor has been deleted")
    
p = Person("Abdalla") 
p1 = Person("Ahmed") 

#Inheritance

class animal:
    def __init__(self):
        print("Hello from animal constructor : ")

    def eat(self):
        print("I eat food ")

    def __del__(self):
        print("Destructor of animal :")

#Super is Ordering constructor
class cat(animal):
    def __init__(self):
        print("Hello from cat constructor : ")
        super().__init__()

    def sound(self):
        print("Meaowwwww ")

    def __del__(self):
        print("Destructor of cat : ")
        super().__del__()

class cat_child(cat):
    def __init__(self):
        print("Hello from cat_child constructor : ")
        super().__init__()

    def sound(self):
        print("Meaow ") 

    def __del__(self):
        print("Destructor of cat_child : ")
        super().__del__()

aziza = cat_child()
aziza.eat()
aziza.sound()

#File OPeration
f = open("file.txt","w")
f.write("Abdalla Nasr /************* ")
f.write("\nAbdalla Nasr 33333333333333333")
f = open("file.txt","r")
print(f.read())
#print(f.read())
#print(f.readlines())
# for line in f:
#     print(line)
#print(f.readline())
#print(f.readline())
#print(f.readline())
f.close()'''

#OS an Shutil Module
import os
import shutil
#Clear
if os.path.exists("project"):
    shutil.rmtree("project")
    print("Folder Deleted")

#Create Folder
os.system("mkdir -p project/src")
os.system("mkdir -p project/tests")
os.system("mkdir -p project/build")
os.system("touch project/src/main.cpp")
os.system("touch project/CMakeLists.txt")

# create main.cpp
fd = open("project/src/main.cpp", "w")
os.write(fd.fileno(),"#include <iostream>\n\
int main(){\n \
std::cout<<\"Hello, World \" << std::endl;\nreturn 0;}".encode())
fd.close()
'''
# create CMakeLists.txt
fd = open("project/CMakeLists.txt","w")
os.write(fd.fileno(),"cmake_minimum_required(VERSION 3.10)\n\
project(helloworld)\n \
add_executable(helloworld src/main.cpp)".encode())
fd.close()'''

#Build
# os.chdir("prject/src")
os.system("g++ project/src/main.cpp -o project/src/Out.o")
os.system("./project/src/Out.o")
print("Done")

#csv
import csv
