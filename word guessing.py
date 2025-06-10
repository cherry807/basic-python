import random

words = ['apple', 'banana', 'grape', 'orange']
word = random.choice(words)
guesses = ''
tries = 6

while tries > 0:
    display = ''.join([letter if letter in guesses else '_' for letter in word])
    print("Word:", display)
    if display == word:
        print("You won!")
        break
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print("Already guessed.")
    elif guess in word:
        guesses += guess
    else:
        tries -= 1
        print(f"Wrong! Tries left: {tries}")
else:
    print(f"You lost! Word was: {word}")
