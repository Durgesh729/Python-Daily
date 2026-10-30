#Take 5 numbers as input, skip any number that is 0 using continue, and calculate the sum of the remaining numbers
n=list(map(int,input("Enter 5 numbers: ").split()))
for i in n:
    if i==0:
        continue
    else:
        t=sum(n)
print(f"sum of {len(n)} number is {t}")
