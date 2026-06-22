# Problem Statement:
# Write a Python program to divide two numbers and handle division by
# zero using try-except.
#
# Input:
# Two integers.
#
# Output:
# Quotient or an error message.
try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Done")
