# Find and print the sum of the Fibonacci series.
n=int(input("Enter number: "))
first=0
second=1
total=0
for i in range(1,n):
    print(total)
    total=first+second
    first=second
    second=total
    if n<=total:
        print("Total Sum is: ",total+0)
        break