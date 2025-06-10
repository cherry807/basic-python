import string

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

print(remove_punctuation("Hello, world!"))
