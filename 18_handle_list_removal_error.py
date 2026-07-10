# Problem Statement:
# Write a Python program to remove an element from a list and handle
# errors if the element does not exist.
#
# Input:
# List and element.
#
# Output:
# Updated list or error message.
try:
    numbers = [10, 20, 30, 40, 50]
    element = int(input("Enter element to remove: "))

    numbers.remove(element)
    print("Updated list:", numbers)
except ValueError:
    print("Element does not exist in the list")
