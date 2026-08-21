"""
Problem Statement:
Read an integer, calculate its square, and display it using factorial-style notation.

Input: An integer n
Output: A formatted expression showing n multiplied by itself
Example: Input: 5 -> Output: 5!=25
"""

# n=int(input("Enter number for factorial"))
# def function(n):
#         print(f"{n}!={n*n}")
# function(n)
n=int(input("Enter number: "))
total=1
for i in range(1,n+1):
    total=i*total
print(total)