"""
Problem Statement:
Find the unique values that are common to two collections of numbers.

Input: Two space-separated sets of integers
Output: The intersection of the two sets
Example: Inputs: 1 2 3 and 2 3 4 -> Output: {2, 3}
"""

n=set(map(int,input("Enter set of number: ").split()))
a=set(map(int,input("Enter set of number: ").split()))
def function(a,n):
        return a.intersection(n)
print(function(a,n))
