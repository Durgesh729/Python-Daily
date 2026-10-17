a, b, c, d, e = map(int, input("Enter 5 numbers with spaces: ").split())
l = [a, b, c, d, e]
total = 0

for i in l:
    if i == 0:
        continue
    total += i

print(total)
