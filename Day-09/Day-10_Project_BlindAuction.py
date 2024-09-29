from replit import clear

clear()
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to the secret auction program.")


bid_info = []
max = 0
winner = ""
iscontinue = 'yes'
while iscontinue == "yes":
    name = input("\nWhat is your name?: ").strip().lower()
    amount = int(input("What's your bid?: $"))
    bid_info.append({"name": name, "amount": amount})
    if amount > max:
        max = amount
        winner = name
    iscontinue = input("Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()
    clear()

print(f"\nThe winner is {winner} with a bid of ${max}.")