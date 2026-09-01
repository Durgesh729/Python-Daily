"""
Problem Statement:
Create a dictionary from entered keys and values, then swap its keys and values.

Input: Space-separated keys and corresponding integer values
Output: The original dictionary and its inverted dictionary
Example: Keys: a b, Values: 1 2 -> Inverted: {1: 'a', 2: 'b'}
"""

n=list(map(str,input("Enter keys with space: ").split()))
a=list(map(int,input("Enter values with space: ").split()))
dictionary=dict(zip(n,a))
print(dictionary,"\n ","Now swapping the position of keys & values")
dictionary1=dict(zip(a,n))
print(dictionary1)
