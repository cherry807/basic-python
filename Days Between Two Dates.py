from datetime import date
d1 = date.fromisoformat(input("Start date (yyyy-mm-dd): "))
d2 = date.fromisoformat(input("End date (yyyy-mm-dd): "))
print("Days between:", abs((d2 - d1).days))
