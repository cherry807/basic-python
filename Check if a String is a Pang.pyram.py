import string
s = input("Enter a sentence: ").lower()
is_pangram = set(string.ascii_lowercase).issubset(set(s))
print("Pangram" if is_pangram else "Not a pangram")
