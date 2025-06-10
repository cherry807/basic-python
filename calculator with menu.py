def calculator():
    while True:
        print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
        choice = input("Choose: ")
        if choice == '5': break
        a, b = float(input("A: ")), float(input("B: "))
        if choice == '1':
            print("Result:", a + b)
        elif choice == '2':
            print("Result:", a - b)
        elif choice == '3':
            print("Result:", a * b)
        elif choice == '4':
            print("Result:", a / b)

calculator()
