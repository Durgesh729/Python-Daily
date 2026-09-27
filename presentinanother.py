"""
Problem Statement:
Check whether every number in the first set is present in the second set.

Input: Two space-separated sets of integers
Output: True or False, followed by the converted data types
Example: Sets: 1 2 and 1 2 3 -> Output begins with True
"""

n=set(map(int,input("Enter number of list: ").split()))
a=set(map(int,input("Enter number of list: ").split()))
def function(n,a):
    return a.issuperset(n)
list1=list(n) 
list2=list(a)
print(function(n,a),type(list1),type(list2))
