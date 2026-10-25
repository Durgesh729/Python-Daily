#Print the square of each number from 1 to n. 
i=0
n=int(input("Enter number: "))
square=0
while i<=n:
    square=i**2
    i+=1
    print(square)