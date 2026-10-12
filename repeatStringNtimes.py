"""
Problem Statement:
Print a personalized greeting a specified number of times.

Input: A name and the number of repetitions
Output: The greeting printed on separate lines
Example: Name: Sam, Times: 2 -> Output: Greeting Mr.Sam twice
"""

# n=input("Enter you name: ")
# a=int(input("How many times you want to repeat your name: "))
# def function(a,n):
#     for _ in range(1,a+1):
#         print(f"Greeting Mr.{n}")
# function(a,n)
a=str(input("Enter name: "))
b=int(input("Enter number: "))
def fun():
    return "\n".join(f"Greeting Mr.{a}" for _ in range(b))
print(fun())
