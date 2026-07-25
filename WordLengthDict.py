"""
Problem Statement:
Create a dictionary that maps each entered word to its length.

Input: Space-separated words
Output: A dictionary of words and their character counts
Example: Input: cat python -> Output: {'cat': 3, 'python': 6}
"""

n=list(map(str,input("Enter keys with space: ").split()))
def function(n):
    a=[len(x) for x in n]
    return dict(zip(n,a))
print(function(n))
  