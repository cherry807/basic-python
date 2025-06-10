lst = list(map(int, input("Enter list: ").split()))
print("Rotated:", [lst[-1]] + lst[:-1])
