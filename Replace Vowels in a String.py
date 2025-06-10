def replace_vowels(s, replacement):
    vowels = "aeiouAEIOU"
    return ''.join(replacement if c in vowels else c for c in s)

print(replace_vowels("Hello World", "*"))
