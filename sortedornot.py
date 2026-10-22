"""
Problem Statement:
Check whether a list of integers is already sorted in ascending order.

Input: Space-separated integers
Output: True if the list is sorted; otherwise False
Example: Input: 1 2 3 -> Output: True
"""

# n=list(map(int,input("Enter number of list with space: ").split()))
# def function(n):
#         if n==sorted(n):
#             return True
#         else:
#             return False
# print(function(n))
n=input("Enter numers: ")
t=list(map(int,n))
l=list(map(int,n))
l.sort()
if t==l:
    print(True)
else:
    print(False)