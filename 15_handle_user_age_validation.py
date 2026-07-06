# Problem Statement:
# Write a Python program to validate user age input and handle invalid
# values using exceptions.
#
# Input:
# Age value.
#
# Output:
# Valid age or error message.
try:
    n=int(input("Enter: "))
    print("age: ",n)
except ValueError:
    print("oo")
