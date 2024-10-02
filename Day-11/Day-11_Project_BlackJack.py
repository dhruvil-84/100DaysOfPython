import random
from replit import clear
from art import logo
from art import win
from art import draw
from art import lose

def deal_card():
    """returns a random card from the deck."""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)

def calculate_score(cards):
    """take a list of cards and return the score calculated from the cards."""
    # A hand with only two cards (an Ace and a 10 or K or Q or J) then its a BlackJack! So return 0.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # If there is an Ace and score is already over 21 then we know Ace has two values 1 and 11; so replace Ace's value with 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(your_total, bot_total):
  if your_total > 21 and bot_total > 21:
    # You both went over. Game Draw
    return f"{draw}"
  elif your_total == bot_total:
    # You both have equal score. Game Draw
    return f"{draw}"
  elif bot_total == 0:
    # You lose because opponent has Blackjack
    return f"{lose}"
  elif your_total == 0:
    # You won with a Blackjack
    return f"{win}"
  elif your_total > 21:
    # Your score went over. You lose (your score overflow)
    return f"{lose}"
  elif bot_total > 21:
    # Opponent score went over. You Won (Opponent score overflow)
    return f"{win}"
  elif your_total > bot_total:
    # Your score is more than Opponent's score. You win.
    return f"{win}"
  else:
    # Opponent's score is more than yours. You lose.
    return f"{lose}"

def play_game():
    print(logo)
    your_cards = [deal_card(), deal_card()]
    bot_cards = [deal_card(), deal_card()]
    iscontinue = 'y'

    while iscontinue == 'y':
        your_total = calculate_score(your_cards)
        bot_total = calculate_score(bot_cards)
        print(f"Your cards: {your_cards}, Current score: {your_total}")
        print(f"Computer's first card: {bot_cards[0]}")

        if your_total == 0 or bot_total == 0 or your_total > 21:
            iscontinue = 'n'
        else:
            temp = 'y'
            while temp == 'y':
                change_card = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()
                if change_card == 'y':
                    your_cards.append(deal_card())
                    temp = 'n'
                elif change_card == 'n':
                    temp = 'n'
                    iscontinue = 'n'
                else:
                    print("Please type 'y' or 'n' only!")
                    
    # Once the user is done; the computer should keep drawing cards as long as it has a score less than 17 making sure computer is not in blackjack(bot_total = 0).
    while bot_total != 0 and bot_total < 17:
        bot_cards.append(deal_card())
        bot_total = calculate_score(bot_cards)

    print(f"\nYour final hand: {your_cards}")
    print(f"Computer's final hand: {bot_cards}")
        
    your_total = calculate_score(your_cards)
    bot_total = calculate_score(bot_cards)
    print(compare(your_total, bot_total))

clear()
temp = 'y'
while temp == 'y':
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
    if play == 'y':
        clear()
        play_game()
    elif play == 'n':
        temp = 'n'
    else:
        print("Please type 'y' or 'n' only!")