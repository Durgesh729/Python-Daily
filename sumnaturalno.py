# Find and print the sum of the first n natural numbers. 
n=int(input("Enter number for sum:"))
total=0
for i in range(1,n+1):
    total=total+i
print("sum of natural numbers ",total)