'''
round() function: round off the number to nearest decimal places.

print(round(8/3, 2))  		# 2.67
print(round(8/3, 5))  		# 2.66667
print(round(5/2, 5))  		# 2.5
print(round(5/2, 2))  		# 2.5
print(round(5/2, 1))  		# 2.5
print(round(5/2, 0))  		# 2.0
print(round(5/2))     		# 2
print(round(5/2, -2)) 		# 0.0
print(round(5/2, -1)) 		# 0.0
print(round(5/2, 0))  		# 2.0
print(round(8/3, 1))  		# 2.7
print(round(8/3, 0))  		# 3.0
print(round(8/3, -1)) 		# 0.0
'''

age = int(input("What is your current age?"))
months = 12 * (90 - age)
weeks = 52 * (90 - age)
days = 365 * (90 - age)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
