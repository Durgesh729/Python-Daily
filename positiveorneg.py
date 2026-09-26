#1.	Write a program to check whether a number is positive or negative. 
while True:   
    n=int(input("Enter number: "))
    if n>0:
        print(f"{n} is positive")
    elif n<0:
        print(f"{n} is negative")
    else:
        print(f"{n} is 0")