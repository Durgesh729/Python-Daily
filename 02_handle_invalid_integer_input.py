# Problem Statement:
# Write a Python program to take integer input from the user and handle
# invalid input errors.
#
# Input:
# User input.
#
# Output:
# Integer value or error message.
while True:
    try:
        n=int(input("Enter number"))
        c=3/n
        print(c)
        break
    except ValueError:
        print("give appropriate number")