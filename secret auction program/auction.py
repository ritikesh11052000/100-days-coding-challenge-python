from art2 import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

name = input("what is your name?: ")
bid = input("What's your bid?: $")
other = input("Are there any other bidders? Type 'yes' or 'no'.")
bidders = {}
def add_bidder(name, bid):
  bidders[name] = bid
add_bidder(name, bid)
while other == "yes":
  name = input("what is your name?: ")
  bid = input("What's your bid?: $")
  other = input("Are there any other bidders? Type 'yes' or 'no'.")
  add_bidder(name, bid)
highest_bid = 0
highest_bidder = ""
for bidder in bidders:
  if int(bidders[bidder]) > highest_bid:
    highest_bid = int(bidders[bidder])
    highest_bidder = bidder
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


