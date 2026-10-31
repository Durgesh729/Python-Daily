#Calculate the sum of all even numbers from 1 up to n. 
n=int(input("Enter number for sum of even no. : "))
count=2
total=0
while count<=n:
    total+=count
    count+=2
print(total)