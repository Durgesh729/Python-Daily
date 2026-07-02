# Problem Statement:
# Write a Python program to demonstrate the use of finally block after
# exception handling.
#
# Input:
# Any operation.
#
# Output:
# Execution result and final message.
try:
    a=10
    b=0
    c=a/b
    print(c)
except IndexError:
    print("Done")
finally:
    print("yes")