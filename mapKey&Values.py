"""
Problem Statement:
Create a dictionary by matching entered keys with corresponding values.

Input: Space-separated keys and space-separated integer values
Output: A dictionary containing the key-value pairs
Example: Keys: a b, Values: 1 2 -> Output: {'a': 1, 'b': 2}
"""

n=list(map(str,input("Enter Key for dictionary: ").split()))
a=list(map(int,input("Enter value for dictionary: ").split()))
def function(n,a):
    return dict(zip(n,a))
print(function(n,a))
