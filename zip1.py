"""
Problem Statement:
Combine two lists by pairing items at the same positions.

Input: Two space-separated lists
Output: A list of paired values
Example: Inputs: a b and 1 2 -> Output: [('a', '1'), ('b', '2')]
"""

# a=list(input("Enter number of list with space").split())
# b=list(input("Enter number of list with space").split())
# def function(a,b):
#     return list(zip(a,b))
# print(function(a,b))
a=list(map(str,input("Enter string: ").split()))
b=list(map(int,input("Enter numbers: ").split()))
l=list(zip(a,b))
print(l)