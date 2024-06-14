#Write a Python program to test whether a passed letter is a vowel or not

VowelLetters = "AEIOUaeiou"

letter = input("Enter a letter : ")

for i in VowelLetters:
    if i == letter:
        flag = True
        break
    else :
        flag = False

if flag == True:
    print("letter is vowel")
else :
    print("letter is not vowel")