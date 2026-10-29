# Calculate and print the sum of the first n natural numbers.
n = int(input("Enter number for sum: "))
count = 1
total = 0
while count <= n:
    total += count
    count += 1
print(f"The sum of the first {n} natural numbers is: {total}")