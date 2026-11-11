"""
Problem Statement:
Store entered numbers in a set and display their unique values.

Input: Space-separated integers
Output: A set containing each distinct value once
Example: Input: 1 2 2 3 -> Output: {1, 2, 3}
"""

n=set(map(int,input("Enter set on number to find unique: ").split()))
def function(n):
    return n.union(n)
print(function(n))
