#Print the Fibonacci series up to the required number of terms.
n=int(input("Enter number: "))
total=0
first=0
second=1
for i in range(0,n+1):
    print(total)
    total=first+second
    first=second
    second=total
    if n<=total:
        break
    