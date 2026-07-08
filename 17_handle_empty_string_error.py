# Problem Statement:
# Write a Python program to check whether a string is empty and handle
# it using exceptions.
#
# Input:
# A string.
#
# Output:
# String value or error message.
try:
    n=""
    if len(n)==0:
        print(n[0])
except IndexError:
    print("oo")