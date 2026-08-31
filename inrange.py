#10.	Write a program to check whether a number is within the range of 1 to 100.
while True:
    n=int(input("Enter number: "))
    if n in range(1,101):print(f"{n} is within range 1 to 100")
    else:print(f"Out of range")