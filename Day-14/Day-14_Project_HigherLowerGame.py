import random
from replit import clear
from game_data import logo
from game_data import vs
from game_data import data

def check(guess, index_A, index_B):
    if guess == 'A':
        return data[index_A]['follower_count'] > data[index_B]['follower_count']
    else:
        return data[index_B]['follower_count'] > data[index_A]['follower_count']

def update_index_A(guess, index_A, index_B):
    if guess == 'A':
        return index_B
    else:
        return index_A

def play():
    clear()
    print(logo)
    score = 0
    index_A = random.randint(0, len(data) - 1)

    discontinue = False
    while not discontinue:
        index_B = random.randint(0, len(data) - 1)
        while (index_A == index_B) or (data[index_A]['follower_count'] == data[index_B]['follower_count']):
            index_B = random.randint(0, len(data) - 1)

        print(f"Compare A: {data[index_A]['name']}, a {data[index_A]['description']}, from {data[index_A]['country']}.")
        print(vs)
        print(f"Against B: {data[index_B]['name']}, a {data[index_B]['description']}, from {data[index_B]['country']}.")

        temp = True
        while temp:
            guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
            if guess == 'A' or guess == 'B':
                temp = False
            else:
                print("Please type 'A' or 'B'")

        cont = check(guess = guess, index_A = index_A, index_B = index_B)
        if cont == True:
            score += 1
            index_A = update_index_A(guess = guess, index_A = index_A, index_B = index_B)
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            discontinue = True
            clear()
            print(f"Sorry, that's wrong. Final score: {score}")

    temp = True
    while temp:
        playagain = input("\nType 'y' to play again, otherwise type 'n': ").strip().lower()
        if playagain == 'y':
            temp = False
            play()
        elif playagain == 'n':
            temp = False
        else:
            print("Please type 'y' or 'n'.")

play()