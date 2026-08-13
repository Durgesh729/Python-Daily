#Print all numbers between a and b that are divisible by 7.
a=int(input("Enter number in between (1 to 20): "))
b=int(input("Enter number 21+ : "))
total=0
for i in range(a,b):
    if i%7==0:
        print(i)