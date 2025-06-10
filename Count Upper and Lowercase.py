s = input("Enter string: ")
u, l = sum(1 for c in s if c.isupper()), sum(1 for c in s if c.islower())
print("Upper:", u, "Lower:", l)
