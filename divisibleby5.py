#5.	Write a program to check whether a number is divisible by 5. 
while True:
    n=int(input("Enter number: "))
    if n%5==0:
        print(f"{n} is divided by 5")
    else: print(f"{n} is not divided by 5")