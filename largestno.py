#. Find the largest digit in the given number. 
a=input("Enter number: ")
i=0
largest=int(a[0])
while i<=len(a)-1:
    if int(a[i])>largest:
        largest=int(a[i])
    i+=1
print(largest)