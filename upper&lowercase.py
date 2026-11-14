#Write a Python program to separate uppercase and lowercase characters from a string
s="I am now Patient".replace(" ","")
print(["Upper Case"]+[i for i in s if i==i.upper()]+["Lower Case"]+[i for i in s if i==i.lower()])