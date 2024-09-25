'''
for loop

for 'variable' in 'iterable':
	# statement 1
	# statement 2
	:
	:
	# statement n
'''

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])

count = 0
sum = 0
for height in student_heights:
	count += 1
	sum += height
print(round(sum / count))

