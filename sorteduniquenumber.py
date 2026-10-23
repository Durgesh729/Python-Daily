"""
Problem Statement:
Build a frequency dictionary to identify and organize unique numbers from a list.

Input: Space-separated integers
Output: A dictionary containing numbers and their occurrence counts
Example: Input: 2 1 2 -> Intended counts: {2: 2, 1: 1}
"""

n=list(input("Enter list of numbers: "))
# print(type(n))
# def function(n):
#     D={}
#     for i in n:
#         if i in n:
#             D.items()+=1
#         else:
J=[n.count(x) for x in n]
print(list(zip(n,J)))


