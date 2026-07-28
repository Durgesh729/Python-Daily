"""
Problem Statement:
Check whether two entered strings contain exactly the same characters in the same order.

Input: Two strings
Output: True if both character lists are identical; otherwise False
Example: Input: cat, cat -> Output: True
"""

# a=list(input("Enter Name: "))
# b=list(input("Enter Name: "))
# def function(a,b):
#     if a==b and len(a)==len(b):
#         return True
#     else :
#         return False
# print(function(a,b))

a,b=map(str,input("Enter strings: ").split())
if a==b and len(a)==len(b):
    print(True)
else:
    print(False)
