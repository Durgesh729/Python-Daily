# Problem Statement:
# Write a Python program to convert list elements into integers and
# handle invalid conversions.
#
# Input:
# List of values.
#
# Output:
# Converted list or error message.
try:
    l=[1,2,3,4,5,"a"]
    y=[]
    for i in l:
        y.append(int(i))
    print(y)
except TypeError:
    print("oo")
except ValueError:
    print("o")