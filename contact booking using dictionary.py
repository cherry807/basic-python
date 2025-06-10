contacts = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contacts[name] = number

def search_contact():
    name = input("Search name: ")
    print("Number:", contacts.get(name, "Not found"))

while True:
    ch = input("Add/Search/Quit: ").lower()
    if ch == 'add':
        add_contact()
    elif ch == 'search':
        search_contact()
    else:
        break
