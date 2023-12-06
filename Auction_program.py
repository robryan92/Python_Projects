import os
from bid_art import logo

#HINT: You can call clear() to clear the output in the console.
print(logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  # bidding_record = {"Angela: 123", "James: 321"}
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if int(bid_amount) > int(highest_bid):
      highest_bid = bid_amount
      winner = bidder
      os.system('cls')
  print(f"The Winner is {winner} with a bid of ${highest_bid}!")

while not bidding_finished:
  name = input("What is your name?\n")
  bid = input("What is your bid? \n$")
  bids[name] = bid
  new_bidder = input("Are there any other people bidding?\n")
  if new_bidder == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif new_bidder == "yes":
    os.system('cls')
  

  
  