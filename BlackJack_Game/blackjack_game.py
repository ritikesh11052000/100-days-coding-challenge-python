from art import logo
import random

print(logo)

user_cards = []
computer_cards = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
    
def deal_initial_cards():
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards)==2:
        return 0
    if 11 in cards and score >21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


deal_initial_cards()
print("User's cards:", user_cards)
print("Computer's cards:", computer_cards)
print("User's score:", calculate_score(user_cards))
print("Computer's score:", calculate_score(computer_cards))