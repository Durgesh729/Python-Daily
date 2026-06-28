# Problem Statement:
# Write a Python program to import a module and handle import errors.
#
# Input:
# Module name.
#
# Output:
# Successful import message or error.
try:
    import numpy1 as np
    arr=np.array([1,2,3])
    print(arr)
except ImportError:
    print("incorrect in import")