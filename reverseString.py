"""
Problem Statement:
Reverse an entered string.

Input: A string
Output: The characters of the string in reverse order
Example: Input: hello -> Output: olleh
"""

n=input("Enter String: ")
def function(n):
    print(n[::-1])
function(n)
