"""
Problem Statement:
Display all even numbers from a list of integers.

Input: Space-separated integers
Output: Each even integer on a new line
Example: Input: 1 2 3 4 -> Output: 2 and 4
"""

# #write a program to find even number ?
# a = input("Enter list of numbers with spaces: ")
# n = list(map(int, a.split()))
# for num in n:
#     if num % 2 == 0: # num %2!=0  for odd logic
#         print(num)

n=list(map(int,input("Enter numbers: ").split()))
for i in n:
    if i%2==0:
        print(i,end=' ')