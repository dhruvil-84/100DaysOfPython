'''
Randomisation:
(Search for the doocumentation of modules in AskPython)

methods of random module in python: (import random)

1. randint(start, end) : returns a random Integer between start and end (both inclusive). This also raises a value error if astart > end.

2. random() : returns the random floating point number between [0.0 to 1.0)  #{0.0 is inclusive and 1.0 is Exclusive.}

3. seed() : 
--> The seed() method is used to initialize the random number generator.
--> The random number generator needs a number to start with (a seed value), to be able to generate a random number.
--> By default the random number generator uses the current system time.
--> NOTE: If you use the same seed value twice you will get the same random number twice.

4. choice() :
--> The choice() method returns a randomly selected element from the specified sequence.
--> The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

5. shuffle() :
--> The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
--> Note: This method changes the original list, it does not return a new list.
'''

import random as r

test_seed = int(input("Create a seed number: "))
r.seed(test_seed) # cannot also be done as random.seed(test_seed)

num = r.randint(0, 1)
if(num == 1):
	print("Heads")
else:
	print("Tails")

# OR

n = round(r.random())
if(n == 1):
	print("Heads")
else:
	print("Tails")