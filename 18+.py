#4.	Write a program to check whether a person is eligible to vote (age ≥ 18). 
while True:
    name=input("Enter name: ")
    n=int(input("Enter age: "))
    if n>=18:
        print(f"{name} is eligible for vote ")
    else:
        print(f"{name} is not eligible for vote")
