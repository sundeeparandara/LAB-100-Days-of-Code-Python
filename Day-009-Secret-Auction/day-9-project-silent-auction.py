from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

def gather_bid():
  name = str(input("What is your name?: "))
  bid = int(input("What's your bid?: $"))
  name_bid_dict[name] = bid

def find_winning_bid(input_bid_dict):
  max_val_key = max(input_bid_dict, key=input_bid_dict.get)
  max_val = max(input_bid_dict.values())
  print(f"The winner is {max_val_key} with a bid of ${max_val}")

name_bid_dict = {}

print(logo)
print("Welcome to the secret auction program.")

other_bidders = 'yes'

while other_bidders == 'yes':
  gather_bid()
  other_bidders = str(input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()
  if other_bidders == 'no':
    break
  else:
    clear()

find_winning_bid(name_bid_dict)