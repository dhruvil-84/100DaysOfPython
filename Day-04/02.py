names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

'''
The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.
'''

import random
print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!")
# OR
print(f"{random.choice(names)} is going to buy the meal today!")