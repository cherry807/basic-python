balance = 1000

while True:
    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        print("Balance:", balance)
    elif choice == '2':
        amount = int(input("Enter amount: "))
        balance += amount
    elif choice == '3':
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient balance")
    elif choice == '4':
        break
