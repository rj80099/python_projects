from art import logo

print(logo)

bidders={}
bidding_finished=False

def find_highest_bidder(bid_record):
  highest_bid=0
  winner =""
  for bidder in bid_record: 
      if bid_record[bidder] > highest_bid:
        highest_bid=bidders[bidder]
        winner=bidder
  print(f'{winner} is the highest bidder among all')

while not bidding_finished:
  bidder_name=input("What is name of the bidder?  ")
  bidder_bid=int(input("What is your bid? $ "))
  bidders[bidder_name]=bidder_bid
  should_continue=input("Are there any other bidders? Type 'Yes' or 'No': ").upper()
  if should_continue == "NO":
     bidding_finished=True
     find_highest_bidder(bidders)

