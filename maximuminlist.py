"""
Problem Statement:
Sort a list of integers and find its largest value.

Input: Space-separated integers
Output: The sorted list followed by its maximum value
Example: Input: 3 1 5 -> Output: [1, 3, 5] and 5
"""

n=list(map(int,input("Enter number of list for finding largest one: ").split()))
# n.sort()
# print(n)
# a=max(n)
# print(a)      
n.sort()
l=max(n)
print(n ,l)