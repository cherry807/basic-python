tasks = []

while True:
    choice = input("Add/View/Remove/Quit: ").lower()
    if choice == 'add':
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == 'view':
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == 'remove':
        num = int(input("Task number to remove: "))
        tasks.pop(num-1)
    elif choice == 'quit':
        break
