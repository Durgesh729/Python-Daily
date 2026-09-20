"""
Problem Statement:
Read a list of integers and print each integer on a separate line.

Input: Space-separated integers
Output: Each integer on a new line
Example: Input: 4 5 6 -> Output: 4, 5, and 6 on separate lines
"""

# n=list(map(int,input("Enter name").split()))
# for i in n:
#     print(i)
n=map(int,input("Enter number of list by spacing: ").split())
for i in n:
    print(i)