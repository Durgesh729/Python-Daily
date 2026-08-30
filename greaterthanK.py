"""
Problem Statement:
Compare the length of a string with a given target length.

Input: A string and an integer target length
Output: A message stating whether the string length reaches or exceeds the target
Example: String: hello, Target: 4 -> Output: String length is greater
"""

# n=list(input("Enter name to check length "))
# a=int(input("Enter number of lenght of string "))
# def function(n,a):
#     if a>len(n):
#         return "String length is not greater is targeted length"
#     else :
#         return "String length is greater is targeted length"
# print(function(n,a))
a=str(input("Enter string: "))
b=int(input("Enter target: "))
if len(a)<b:
    print("targest length greater than string")
elif len(a)>b:
    print("String length greater than target")
else:
    print("both having same length")