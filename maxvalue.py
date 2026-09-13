"""
Problem Statement:
Sort a sequence of digits and display the largest digit.

Input: A sequence of digits
Output: The largest digit in the sequence
Example: Input: 3152 -> Output: 5
"""

# n=input("Enter number of list:")
# a=list(map(int,n))
# def maxvalue(a):
#        return a.sort()
# b=len(a)
# print(a[b-1])
n = set(map(int, input("Enter numbers: ").split()))
n.remove(max(n))
print(max(n))
