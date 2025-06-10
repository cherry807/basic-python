base, exp = map(int, input("Base and exponent: ").split())
result = 1
for _ in range(exp):
    result *= base
print("Result:", result)
