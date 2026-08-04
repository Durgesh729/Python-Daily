"""
Problem Statement:
Count how many times each target number appears in a list.

Input: A list of integers followed by target integers
Output: The occurrence count of each target
Example: List: 1 2 2 3, Targets: 2 3 -> Output: 2 and 1
"""

# a=list(map(int,input("Enter number of list").split()))
# b=list(map(int,input("Enter target numbers").split()))
# for target in b:
#     print(a.count(target))
a=list(map(int,input("Enter sequence of numbers: ").split()))
b=list(map(int,input("Enter sequence of numbers: ").split()))
for i in b:
    print(a.count(i))