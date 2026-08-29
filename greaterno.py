#3.	Write a program to find the greater number between two numbers. 
while True:
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    if a>b:
        print(f"{a} is greater than {b}")
    elif b>a:
        print(f"{b} is greater than {a}")
    else:
        print(f"both are same")