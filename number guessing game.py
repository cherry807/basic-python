import random

number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess the number: "))
    tries += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! Tries: {tries}")
        break
