n = int(input("Enter number: "))
print("Harshad" if n % sum(int(d) for d in str(n)) == 0 else "Not Harshad")
