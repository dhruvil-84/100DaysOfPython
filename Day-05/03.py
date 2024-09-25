'''
range() function:

using range() function in forloop:

for 'variable' in range(start(inclusive), stop(exclusive), step):
	# statement 1
	# statement 2
	:
	:
	# statement n

'''

total = 0
for i in range(2, 101, 2):
	total += i
print(total)