"""
Problem Statement:
Find dictionary entries whose values are greater than a given threshold.

Input: An integer threshold
Output: A list of key-value pairs above the threshold
Example: Threshold: 2 -> Output: [('c', 3), ('D', 4)]
"""

n = {"a":1, "b":2, "c":3, "D":4}
k = int(input("Enter number: "))

def keys_below(d, threshold):
    return [(key , val) for key, val in d.items() if val > threshold]

print(keys_below(n, k))
