"""
Problem Statement:
Read a sequence of digits, convert them to integers, and display them in sorted order.

Input: A sequence of digits
Output: A list of the digits arranged from smallest to largest
Example: Input: 3142 -> Output: [1, 2, 3, 4]
"""

# user_input = input("Enter a list of numbers ")

       
# lst = list(map(int,user_input))          

# lst.sort()                       

# print(lst)
n=input("Enter number: ")
l=list(map(int,n))
l.sort()
print(l)