# Problem Statement:
# Write a Python program to divide numbers inside a loop and handle
# division by zero errors.
#
# Input:
# List of divisors.
#
# Output:
# Division results or error messages.
try:
    for i in range(10,-1,-1):
        print(10/i)

except ZeroDivisionError:
    print("oo")