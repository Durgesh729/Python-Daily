"""
separate two lists by pairs items of the same positions.

Input: A list of paired values
Output: Two space-separated lists
Example: Inputs: [('a', '1'), ('b', '2')] -> Output: a b and 1 2
"""
l=[('a', '1'), ('b', '2')]
p=list(zip(*l))
print(p)