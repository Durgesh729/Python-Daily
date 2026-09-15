"""
Problem Statement:
Merge two lists of integers and sort the combined list.

Input: Two space-separated lists of integers
Output: One sorted list containing all values
Example: Inputs: 3 1 and 4 2 -> Output: [1, 2, 3, 4]
"""

n=list(map(int,input("Enter list of number: ").split()))
n1=list(map(int,input("Enter list of number: ").split()))
# n.extend(n1)
# n.sort()
# print(n)
l=max(n)
l1=max(n1)
n.sort()
n1.sort()
if l>l1:
    print(n1+n)
else:
    print(n+n1)