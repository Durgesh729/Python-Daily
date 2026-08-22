#Calculate and print the factorial of every number from 1 to n.
n=int(input("Enter number: "))
total=1
for i in range(1,n+1):
    total=total*i
    print(i,":",total)
