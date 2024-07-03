#All string built-in functions
string = "abdalla"
string1 = "ABDALLA"
string2 = "abdalla nasr farag ali ahmed rabea"

#Capitalize first letter
print(string.capitalize())
#Make it at lower case
print(string1.casefold())
#Put it at the center of this number "15" and "*" at wing
print(string.center(15,'*'))
#Count number of this letter in range('letter',start,end)
print(string2.count('a',8))
#Capitalize string
print(string.upper())
#Return index of this letter
print(string.index('a'))

#All dictionary built-in functions
dic = {
    "Name" : "Abdalla",
    "Age" : 22,
    "Country" : "Egypt",
    "Favorit Person" : "Nada"
}
#print all keys and values
print(dic)
#Clear all keys and values
#print(dic.clear())

#Retrun specific value using key
print(dic.get("Name"))
print(dic.get("Favorit Person"))
#print all keys and values
print(dic.items())
#Pop specific value using key
print(dic.pop("Name"))
print(dic)
#
dic["Name"] = "Abdalla"
print(dic)