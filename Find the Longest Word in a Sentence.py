def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("Python is a powerful programming language"))
