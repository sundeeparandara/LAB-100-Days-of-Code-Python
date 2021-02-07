from art import logo
from art import vs
from game_data import data
import random
from replit import clear

def assess(a_follower_count,b_follower_count,user_answer):

  if a_follower_count > b_follower_count:
    correct_answer = 'A'
  else:
    correct_answer = 'B'

  if correct_answer == user_answer:
    return True
  else:
    return False

def game(a_dict,b_dict):
  
  answer_correct = True
  a_follower_count = a_dict['follower_count']
  b_follower_count = b_dict['follower_count']
   
  print(f"Compare A: {a_dict['name']}, a {a_dict['description']}, from {a_dict['country']}")
  print(vs)
  print(f"Compare B: {b_dict['name']}, a {b_dict['description']}, from {b_dict['country']}")
  user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
  answer_correct = assess(a_follower_count,b_follower_count,user_answer)
  
  global USER_SCORE
  if answer_correct == True:
    clear()
    print(logo)
    USER_SCORE += 1
    print(f"You are right! Current score: {USER_SCORE}")
    a_dict = b_dict
    b_dict = random.choice(data)
    game(a_dict,b_dict)
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {USER_SCORE}")


USER_SCORE = 0
print(logo)
a_dict = random.choice(data)
b_dict = random.choice(data)

game(a_dict,b_dict)      

