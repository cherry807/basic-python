s = input("Enter a sentence: ")
reversed_words = ' '.join(word[::-1] for word in s.split())
print("Reversed words:", reversed_words)
