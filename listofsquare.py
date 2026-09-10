"""
Problem Statement:
Calculate and display the square of every number in a list.

Input: Space-separated integers
Output: The square of each integer
Example: Input: 2 3 4 -> Output: 4 9 16
"""

# n=list(map(int,input("Enter list of number with space: ").split()))
# def function():
#     for x in n:
#          print(x**2,end=" ")
# function()
n=list(map(int,input("Enter numbers by spacing: ").split()))
for i in range(1,len(n)+1):
    print(i**2,end=' ')