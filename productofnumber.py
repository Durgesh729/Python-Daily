#  Find and print the product of all digits of a given number. 
n=input("Enter large number for product of each digit: ")
total=1
i=0
while i<len(n):
    total*=int(n[i])
    i+=1
print(total)
    
