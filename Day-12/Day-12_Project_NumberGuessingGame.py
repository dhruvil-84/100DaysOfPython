import random
import art
from replit import clear

def check(your_num, bot_num):
    if your_num > bot_num:
        return "Too High.\nGuess again."
    else:
        return "Too Low.\nGuess again."
    
def play():
    clear()
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = 0
    
    temp = True
    while temp:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if difficulty == "easy":
            attempts = 10
            temp = False
        elif difficulty == "hard":
            attempts = 5
            temp = False
        else:
            print("Please type 'easy' or 'hard'")
    
    bot_num = random.randint(1, 100)
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        your_num = int(input("Make a guess: "))
        if your_num == bot_num:
            print(art.win)
            break
        else:
            print(check(your_num = your_num, bot_num = bot_num))
            attempts -= 1
    
    if attempts == 0:
        print(art.lose)
        print(f"The Number was {bot_num}\n")
    
    ask = True
    while ask:
        playagain = input("Type 'y' to play again, otherwise type 'n': ").strip().lower()
        if playagain == 'y':
            ask = False
            clear()
            play()
        elif playagain == 'n':
            ask  = False
        else:
            print("Please type 'y' or 'n' only.")

play()