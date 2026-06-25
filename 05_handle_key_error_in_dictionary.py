# Problem Statement:
# Write a Python program to access dictionary values and handle missing
# key errors.
#
# Input:
# Dictionary and key.
#
# Output:
# Value or error message.
try:
    d={"a":1,"b":2,"c":3}
    print(d[3])
except KeyError:
    print("o")