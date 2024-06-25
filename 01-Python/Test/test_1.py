#Strings

print("Hello")
print('Hello')   
print('Abdalla "Nasr" ') # For using douple qoute in print
print('''Hello''')

#Datatypes
x = 5
print(x)
print(id(x))
print(type(x))
x = "Abdalla"
print(x)
print(id(x))
print(type(x))

x,y,z = 1,2,3
print(x)
print(y)
print(z)

#list
print("\nList")
x = ["Abdalla",1,2,3,4,5,6]
print(x[0:5])  #slice from 0 to 4 , 5 is execluded 
print(x[0:5:2])  #slice with step 2
print(x[0:]) #from 0 to end
print(x[0::2]) #from 0 to end with step 2
print(x[-1]) #last element
x[1] = 55 #mutable

#tuple
print("\nTuple")
x = ("Abdalla",1,2,3,4,5,6,7,8)
print(x[0:5])  #slice from 0 to 4 , 5 is execluded 
print(x[0:5:2])  #slice with step 2
print(x[0:]) #from 0 to end
print(x[0::2]) #from 0 to end with step 2
print(x[-1]) #last element
#x(1) = 55 #immutable

#dictionary
print("\nDictionary")
dic = {
    "brand" : "Ford",
    "model" : "x55",
    "year" : 2002
}
print(dic) #print all dictionary
print(dic["brand"]) #print specific key 
print(dic.keys()) #print all keys
print(dic.values()) #print all values
print(len(dic))   #length of dictionary

#set
print("\nSet")

thisset = {"Abdalla","Nasr", "Farag"}
print(set(thisset))

#Range
print("\nRange")
for i in range(0,5):
    print(i,end = ","  )
print("\n")

#Take input
input_name = input("Please enter your name : ")
print("Hello, " + input_name)
age = int(input("Enter your age : "))
print("Age is : " + str(age))

#in , not in

print(1 in (1,2,3,4,5,6)) #print True
print(1 not in (1,2,3,4,5,6)) #print False
print(8 in (1,2,3,4,5,6)) #print False
print(8 not in (1,2,3,4,5,6)) #print True


#is , is not

a = [10]
b = [10]
print(id(a))
print(id(b))
if a is b :
    print("a and b have same identity")

if a == b :
    print("a and b are equal")

#if condition

x = False

if x == True :
    print("X is True")

elif x == False :
    print("X is False")

print("Hello")

#Short hand if
a = 10 
b = 15
print("A is greater than B") if a > b else print("B is smaller than A")

