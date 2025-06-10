rows = int(input("Enter number of rows: "))
for i in range(1, rows+1):
    print(' '.join(str(x) for x in range(1, i+1)))
