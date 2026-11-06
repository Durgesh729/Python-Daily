"""
Problem Statement:
Use a function to calculate and display the sum of a list of integers.

Input: Space-separated integers
Output: The sum of all entered integers
Example: Input: 2 3 5 -> Output: 10
"""

n=list(map(int,input("Enter list of number: ").split()))
def function(n):
    print(sum(n))
function(n)
