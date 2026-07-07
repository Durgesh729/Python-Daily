# Problem Statement:
# Write a Python program to raise an exception if the entered number is
# negative.
#
# Input:
# An integer.
#
# Output:
# Number value or custom error message.
while True: 
    try:
        n=input("Enter number: ")
        if n.isalpha():
            print("Enter number: ")
        elif int(n)<0:
            print(int(n)/0)
    except ZeroDivisionError:
        print("oo")