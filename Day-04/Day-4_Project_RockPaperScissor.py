import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if (user_choice >= 0) and (user_choice < 3):
	bot = random.randint(0, 2)
	print("\nYour choice is: \n", game_images[user_choice])
	print("Computer's choice is: \n", game_images[bot])	
	if (user_choice == bot):
		print("It's a draw")
	elif ((user_choice == 0) and (bot == 1)) or ((user_choice == 1) and (bot == 2)) or ((user_choice == 2) and (bot == 0)):
		print("You lose")
	else:
		print("You win!")
else:
	print("Please Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")