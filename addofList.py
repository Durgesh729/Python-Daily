"""
Problem Statement:
Add corresponding numbers from two lists.

Input: Two space-separated lists of integers
Output: A list containing the sum of each pair
Example: Inputs: 1 2 3 and 4 5 6 -> Output: [5, 7, 9]
"""

# n=list(map(int,input("Enter list of number: ").split()))
# a=list(map(int,input("Enter list of number: ").split()))
# def function(n,a):
#     return [x + y for x, y in zip(a, n)]
# print(function(n,a))
l=[1,2,3,4]
p=[2,3,4,5]
print(list(a+b for a,b in  zip(l,p)))
