"""
Problem Statement:
Count the occurrences of every character in an entered string.

Input: A string
Output: A list pairing each character with its total count
Example: Input: aba -> Output: [('a', 2), ('b', 1), ('a', 2)]
"""

a = list(input("Enter name: "))
counts = [a.count(ch) for ch in a]
# counts = []

# for ch in a:
#     counts.append(a.count(ch))
print(list(zip(a, counts)))
