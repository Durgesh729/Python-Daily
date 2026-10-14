# Reverse the given number and print the reversed value.
n=input("Enter number to reverse : ")
i=len(n)-1
reverse=""
while i>=0:
    reverse+=n[i]
    i-=1
print(reverse)
