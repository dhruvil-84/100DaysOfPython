import random
from Hangman_resources import stages
from Hangman_resources import word_list
from Hangman_resources import won
from Hangman_resources import game_over

chosen_word = list(random.choice(word_list))
temp = "".join(chosen_word)
exit = len(chosen_word)
guess_word = []
for i in chosen_word:
    guess_word.append('_')
    # OR
    # guess_word += "_"

life = len(stages) - 1

while ((life != 0) and (exit != 0)):
    guess = input("\nGuess a letter: ").lower()
    if guess in chosen_word:
        for i in range(0, len(chosen_word)):
            if guess == chosen_word[i]:
                guess_word[i] = chosen_word[i]
                chosen_word[i] = "_"
                exit -= 1
        print("")
        for i in guess_word:
            print(i, end = " ")
        print(f"\n{stages[life]}")
    else:
        for i in guess_word:
            print(i, end = " ")
        life -= 1
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life. Your Life is {life}")
        print(f"{stages[life + 1]}")

if life == 0:
    print(f"{game_over}")
    print(f"The word was '{temp}'.")
else:
    print(f"{won}")