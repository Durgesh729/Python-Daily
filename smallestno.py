#Find the smallest digit in the given number. 
a=input("Enter number: ")
i=0
smallest=int(a[0])
while i<=len(a)-1:
    if int(a[i])<smallest:
        smallest=int(a[i])
    i+=1

print(smallest)