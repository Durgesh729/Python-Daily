# Problem Statement:
# Write a Python program to add two variables and handle incompatible
# data type errors.
#
# Input:
# Two variables.
#
# Output:
# Sum or error message.
try:
    a=input("Enter: ") # here should int()
    b=5
    c=b+a
    print(c)
except TypeError:
    print("oo")