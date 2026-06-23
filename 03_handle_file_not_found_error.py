# Problem Statement:
# Write a Python program to open and read a file while handling file not
# found exceptions.
#
# Input:
# File name.
#
# Output:
# File content or error message.
try:
    with open("f.txt","r") as file:
        file.read()
except FileNotFoundError:
    print("oo")