#2.	Write a program to check whether a number is even or odd. 
while True:
    n=int(input("Enter number: "))
    if n%2==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")