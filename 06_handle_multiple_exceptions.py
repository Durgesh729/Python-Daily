# Problem Statement:
# Write a Python program to handle both value errors and zero division
# errors.
#
# Input:
# Two user inputs.
#
# Output:
# Result or appropriate error message.
try:
    n=int(input("Enter: "))
    c=10/n
    print(c)
except ValueError:
    print("t")
except ZeroDivisionError:
    print("b")