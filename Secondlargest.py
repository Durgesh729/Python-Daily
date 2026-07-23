"""
Problem Statement:
Find the largest number in a list and display the number immediately below it.

Input: Space-separated integers
Output: One less than the maximum value
Example: Input: 2 5 8 -> Output: 7
"""

n=list(map(int,input("Enter number of list: ").split()))
n.remove(max(n))
def function(n):
    print(max(n))
function(n)
