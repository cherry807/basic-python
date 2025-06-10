from collections import Counter

text = input("Enter text: ")
words = text.split()
freq = Counter(words)

for word, count in freq.items():
    print(f"{word}: {count}")
