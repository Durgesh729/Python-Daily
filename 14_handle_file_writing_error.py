# Problem Statement:
# Write a Python program to write data into a file and handle file
# operation errors.
#
# Input:
# File name and text.
#
# Output:
# Success or error message.
with open("File.txt","w") as file:
    file.write("yes")
try:
    with open("File1.txt","r") as file1:
        print(file1.read())
except FileNotFoundError:
    print("oo")
    