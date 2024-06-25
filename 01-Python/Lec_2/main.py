import Firefox

lis = [Firefox.youtube,Firefox.facebook,Firefox.x,Firefox.instagram,Firefox.whatsapp]
print("Menu: \n1-Youtube \n2-Facebook \n3-X \n4-Instagram \n5-Whattsapp")

choise = int(input("Enter youre choise : "))

Firefox.Firefox(lis[choise-1])