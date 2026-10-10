"""
Problem Statement:
Process a list of integers and keep its non-negative values.

Input: Space-separated integers that may include negative values
Output: The resulting list after processing non-negative values
Example: Input: -2 0 3 -> Non-negative values: 0 and 3
"""

# n=list(map(int,input("Enter number of list with negative number: ").split()))
# def function(n):
#     for i in n:
#         if i>=0:
#             n.append(i) 
#     return n
# print(function(n))
n=list(map(int,input("Enter numbes by spacing: ").split()))
for i in n:
    if i>0:
        print(i,end=' ')