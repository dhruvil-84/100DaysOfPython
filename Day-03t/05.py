print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

total_true = (name1 + name2).lower().count('t') + (name1 + name2).lower().count('r') + (name1 + name2).lower().count('u') + (name1 + name2).lower().count('e')

total_love = (name1 + name2).lower().count('l') + (name1 + name2).lower().count('o') + (name1 + name2).lower().count('v') + (name1 + name2).lower().count('e')

score = int(str(total_true) + str(total_love))

if (score < 10) or (score > 90):
	print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
	print(f"Your score is {score}, you are alright together.")
else:
	print(f"Your score is {score}.")