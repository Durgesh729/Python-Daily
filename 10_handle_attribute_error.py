# Problem Statement:
# Write a Python program to access an invalid attribute of an object and
# handle attribute errors.
#
# Input:
# Object and attribute name.
#
# Output:
# Attribute value or error message.
try:
    text="right"
    for i,v in enumerate(dir(text)):# dir() use to Prints all valid attributes and methods available for an object.
        print(i,":",v)
    text.append(fot)#here we can't append it because its not string method
except AttributeError:
    print("AttributeError")