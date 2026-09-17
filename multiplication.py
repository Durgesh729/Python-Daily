# Print the multiplication table of a given number from n × 1 to n × 10.
n=int(input("Enter number for multiplication table: "))
count=1
while count<11:
    print(f"{count} x {n} = {count*n}")
    count+=1