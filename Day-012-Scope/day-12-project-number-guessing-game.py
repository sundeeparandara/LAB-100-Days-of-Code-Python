#NUMBER GUESSING GAME

import random


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number_actual = random.randint(1,100)

difficult_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficult_level == 'easy':
  number_of_attempts = 10
elif difficult_level == 'hard':
  number_of_attempts = 5
else:
  print("You didn't follow the instructions.\nYou get one shot."
  )
  number_of_attempts = 1

def assess_guess(guess,actual):
  state = ""
  if guess == actual:
    print("You guessed right!\nVICTORY!")
    state = "WIN"
  elif guess < actual:
    print("Too low.")
    state = "LOSE"
  elif guess > actual:
    print("Too high.")
    state = "LOSE"
  return state

while not number_of_attempts == 0:
  print(f"You have {number_of_attempts} attempt(s) remaining to guess the number.")
  number_of_attempts -= 1
  number_guess = int(input("Make a guess: "))
  state = assess_guess(number_guess, number_actual)
  if state == "WIN":
    print("GAME OVER")
    break
  elif state == "LOSE" and number_of_attempts == 0:
    print("You've run out of guesses.")
    print(f"The correct answer is: {number_actual}")
    print("DEFEAT\nGAME OVER")

    break
  else:
    print("Guess again.")
