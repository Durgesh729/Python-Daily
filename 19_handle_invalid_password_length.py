# Problem Statement:
# Write a Python program to validate password length and raise an
# exception for short passwords.
#
# Input:
# Password string.
#
# Output:
# Valid password message or error.
try:
    n=input("Enter password: ")
    if len(n)<=5:
        c=n[6]
    else:
        c=n[6]
except IndexError:
    print("oo")