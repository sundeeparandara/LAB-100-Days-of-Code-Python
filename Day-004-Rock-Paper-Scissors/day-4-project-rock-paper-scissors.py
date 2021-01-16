rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

hands = [rock,paper,scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

outcome = "IDK"

if ((human_choice > 2) | (human_choice < 0)):
  outcome = "IDK"
  print(outcome)
else:
  if human_choice == computer_choice:
    outcome = "It is a draw"
  elif ((human_choice == 0) & (computer_choice == 2)):
    outcome = "You win"
  elif ((human_choice == 1) & (computer_choice == 0)):
    outcome = "You win"
  elif ((human_choice == 2) & (computer_choice == 1)):
    outcome = "You win"
  else:
    outcome = "You lose"

  print("\n")
  print(hands[human_choice])
  print("\n")
  print("Computer chose:")
  print("\n")
  print(hands[computer_choice])
  print("\n")
  print(outcome)
  #print("\n")
print("_")