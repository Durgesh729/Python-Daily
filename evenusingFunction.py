"""
Problem Statement:
Use a function to collect and display the even numbers from a list.

Input: Space-separated integers
Output: A list of even numbers, or Odd Number when no even value exists
Example: Input: 1 2 4 -> Output: [2, 4]
"""

n=list(map(int,input("Enter list of number: ").split()))
def function(n):
        evenNO=[x for x in n if x % 2==0]
        if evenNO:
            print(evenNO)
        else:
            print("Odd Number")
            
function(n)




        
