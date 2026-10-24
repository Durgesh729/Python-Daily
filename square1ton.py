#Print the square of each number from 1 to n.
n=int(input("Enter number: "))
total=0
for i in range(1,n+1):
    total=i**2
    print(total)