print("Armstrong number" if int(n := input("Enter number: ")) == sum(int(digit) ** len(n) for digit in n) else "Not an Armstrong number")
