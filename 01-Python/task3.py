#Write a Python program to count the number 4 in a givin linst

x = [1,2,3,4,5,6,7,8,9,4,5,4,6,2,1,4]
count = 0
for i in x :
    if i == 4:
        count+=1
    i+=1
print(count)    

#another way
count = x.count(4)
print(count)