"""
Problem Statement:
Print the multiplication table of a number from 1 to 10.

Input: An integer n
Output: Ten multiplication expressions for n
Example: Input: 3 -> Output begins with 1x3=3
"""

# n=int(input("Enter number for table"))
# for i in range(1,11):
#     print(f"{i}x{n}={i*n}")
n=int(4)
for i,v in enumerate(range(n,n*10+1,n)):
    print(f"{n}X{i+1}={v}")