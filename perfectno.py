#. Check whether the given number is a Perfect number. 
n=int(input("Enter number to check perfect: "))
total=0
i=1
while i<n:
    if n%i==0:
        total=total+i
    i+=1

if total==n:
    print("it is perfect number")
else:
    print("it is not perfect number")
