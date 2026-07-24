"""
Problem Statement:
Calculate the sum of all integers in a list.

Input: Space-separated integers
Output: The total of the integers
Example: Input: 1 2 3 4 -> Output: 10
"""

# n=input("Enter a list of number with  spaces")
# a=list(map(int,n.split()))
# def function(a):
#      return sum(a)
# print(sum(a))
n=list(map(int,input("Enter numbers by spacing: ").split()))
print(sum(n))