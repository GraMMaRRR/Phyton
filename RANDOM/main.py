import random


low = 1
high = 100
options = ("Rock", "Paper", "Scissors")
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# number = random.random()
# number = random.randint(low, high)
# choice = random.choice(options)
# random.shuffle(cards)

# -------------- NUMBER GUESSING GAME --------------

import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
   guess = int(input(f"Enter a number between ({low} - {high}): "))
   guesses += 1

   if guess < number:
       print(f"{guess} is too low")
   elif guess > number:
       print(f"{guess} is too high")
   else:
       print(f"{guess} is correct!")
       break

print(f"This round took you {guesses} guesses")