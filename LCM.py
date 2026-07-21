# Find the LCM (Least Common Multiple) of the given numbers. 
# Find LCM of two numbers using for loop

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

greater = max(a, b)

for i in range(greater, (a * b) + 1):
    if i % a == 0 and i % b == 0:
        print("LCM =", i)
        break