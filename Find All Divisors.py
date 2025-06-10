n = int(input("Enter number: "))
print("Divisors:", [i for i in range(1, n+1) if n % i == 0])
