def count_characters(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    digits = sum(1 for c in s if c.isdigit())
    special = sum(1 for c in s if not c.isalnum())
    return upper, lower, digits, special

print(count_characters("Hello123@#"))
