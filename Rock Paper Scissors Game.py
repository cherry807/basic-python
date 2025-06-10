import random

options = ['rock', 'paper', 'scissors']
user = input("Enter rock/paper/scissors: ").lower()
comp = random.choice(options)

print(f"Computer chose: {comp}")
if user == comp:
    print("It's a tie!")
elif (user == 'rock' and comp == 'scissors') or \
     (user == 'paper' and comp == 'rock') or \
     (user == 'scissors' and comp == 'paper'):
    print("You win!")
else:
    print("You lose!")
