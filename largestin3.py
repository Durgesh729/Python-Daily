#8.	Write a program to find the largest among three numbers. 
while True:
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    c=int(input("Enter number: "))
    if a<c and b<c:print(f"{c} is greater than {a} & {b}")
    elif a<b and c<b:print(f"{b} is greater than {a} & {c}")
    elif c<a and b<a:print(f"{a} is greater than {b} & {c}")
    else :print("all numbers are same")