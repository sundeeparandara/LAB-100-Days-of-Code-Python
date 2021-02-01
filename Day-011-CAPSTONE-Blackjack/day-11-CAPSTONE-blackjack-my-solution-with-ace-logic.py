############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#######################################
########## MY SOLUTION ################
#######################################

import random
from art import logo
from replit import clear

def win_logic(user_hand_total, dealer_hand_total):
  if (user_hand_total > 21) & (dealer_hand_total > 21):
    if user_hand_total < dealer_hand_total:
      print("You win 😎")
    elif user_hand_total == dealer_hand_total:
      print("Draw 🤯")
    else:
      print("You lose 😭")
  elif (user_hand_total <= 21) & (dealer_hand_total <= 21):
    if user_hand_total > dealer_hand_total:
      print("You win 😎")
    elif (user_hand_total == dealer_hand_total):
      print("Draw 🤯")
    else:
      print("You lose 😭")
  elif (user_hand_total > 21) & (dealer_hand_total <= 21):
    print("You went over. You lose 😭")
  elif (user_hand_total <= 21) & (dealer_hand_total > 21):
    print("You win 😎")
  else:
    print("!!!CHECK LOGIC!!!")

def ace_logic(list_of_cards):
  new_list_of_cards = []
  if (11 in list_of_cards) & (sum(list_of_cards) > 21):
    for card in list_of_cards:
      if card == 11:
        new_list_of_cards.append(1)
        print("\tAn Ace was drawn, and declared as '1' instead of '11'")
      else:
        new_list_of_cards.append(card)
  else:
    new_list_of_cards = list_of_cards
  return new_list_of_cards

def blackjack():

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user_hand = []
  dealer_first_card = 0
  dealer_hand = []
  user_hand_total = 0
  dealer_hand_total = 0

  user_hand.append(random.choice(cards))
  user_hand.append(random.choice(cards))
  user_hand = ace_logic(user_hand)
  user_hand_total = sum(user_hand)

  dealer_first_card = random.choice(cards) 
  dealer_hand.append(dealer_first_card)
  dealer_hand = ace_logic(dealer_hand)
  dealer_hand_total = sum(dealer_hand)

  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    print(logo)
    print(f"\tYour cards: {user_hand}, current score: {user_hand_total}")
    print(f"\tComputer's first card: {dealer_first_card}")
    while input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
      user_hand.append(random.choice(cards))
      user_hand = ace_logic(user_hand)
      user_hand_total = sum(user_hand)
      if user_hand_total <= 21:
        print(f"\tYour cards: {user_hand}, current score: {user_hand_total}")
        print(f"\tComputer's first card: {dealer_first_card}")
      else:
        break

    while dealer_hand_total < 17:
      dealer_hand.append(random.choice(cards))
      dealer_hand = ace_logic(dealer_hand)
      dealer_hand_total = sum(dealer_hand)
    
    print(f"\tYour final hand: {user_hand}, final score: {user_hand_total}")
    print(f"\tComputer's final hand: {dealer_hand}, final score: {dealer_hand_total} ")
    win_logic(user_hand_total,dealer_hand_total)
    blackjack()

blackjack()