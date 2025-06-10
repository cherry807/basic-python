n = int(input("Enter number: "))
print("Perfect" if sum(i for i in range(1, n) if n % i == 0) == n else "Not perfect")
