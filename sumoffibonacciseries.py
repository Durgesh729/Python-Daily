#Find and print the sum of the Fibonacci series up to n terms. 
first=0
second=1
i=0
n=int(input("Enter number :"))
total=0
while i<n:
    total=total+first
    next=first+second
    first=second
    second=next
    i+=1

    if n<=first:
        break
print("sum is", total)
