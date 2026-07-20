#. Find the HCF (Highest Common Factor) of the given numbers.
a=int(input("Enter number: "))
b=int(input("Enter number: "))
hcf=1
n=0
if a>b:
    n=b
else:
    n=a
for i in range(1,n+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)