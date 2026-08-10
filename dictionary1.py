"""
Problem Statement:
Display the keys and values of a dictionary and report whether any value is missing.

Input: A predefined dictionary
Output: Lists of keys and values, plus a warning if a value is None
Example: {'a': 1, 'b': None} -> Output includes Values not found
"""

dictionary = {"a":1,"b":2,"c":3, "d": None}
# print(list(dictionary.keys()))
# print(list(dictionary.values()))

# if any(v is None for v in dictionary.values()):
#     print("\nValues not found")
if None in dictionary.values():
         print("include value not found")