#6.	Write a program to check whether a given year is a leap year or not. 
while True:
    n=int(input("Enter number: "))
    if n%4==0:
        print(f"{n} is leap year")
    else: print("not leap year")