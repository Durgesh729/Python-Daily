#9.	Write a program to assign grades based on marks: 90 and above → A  75 to 89 → B  50 to 74 → C Below 50 → Fail 
while True:
    n=int(input("Enter number: "))
    if 90<=n:print("Grade A") 
    elif n in range(75,90):print("Grade B")
    elif n in range(50,75):print("Grade c")
    else :print("Fail")