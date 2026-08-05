"""
Problem Statement:
Count how many positive numbers are present in a list.

Input: Space-separated integers
Output: The number of integers greater than zero
Example: Input: -2 4 0 7 -> Output: 2
"""

# n=input("Enter number to count positive number")
# a=list(map(int,n.split()))
# count=0
# for num in a:
#     if num>0:
#        c=count=count+1
# print(c)

n=map(int,input("Enter numbers by space: ").split())
l=[]
t=list()
for i in n:
    if 0<i:
        l.append(i)
print(l,type(t))