import string
s = input("Enter a string: ")
cleaned = ''.join(ch for ch in s if ch not in string.punctuation)
print("Without punctuation:", cleaned)
