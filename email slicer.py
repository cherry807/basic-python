def email_slicer(email):
    username, domain = email.split("@")
    print(f"Username: {username}")
    print(f"Domain: {domain}")

email = input("Enter your email: ")
email_slicer(email)
