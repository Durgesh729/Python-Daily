# Problem Statement:
# Write a Python program to access an element from a list and handle
# index out of range errors.
#
# Input:
# List and index value.
#
# Output:
# Element value or error message.
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("o|o")