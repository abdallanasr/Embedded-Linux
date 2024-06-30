#Dictionary

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
