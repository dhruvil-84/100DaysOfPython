'''
#------------------------------------------------------------------------------------------------------------

if..elif..else statements.

if condition1:
	# do this if condition1 is True.
elif condition2:
	# do this if condition2 is True.
elif condition3:
	# do this if condition3 is True.
else:
	# do this if condition1, condition2 and condition3 is False.

#------------------------------------------------------------------------------------------------------------

nested if..else statements:

if condition1:
	if condition2:
		# do this if condition1 is True and condition2 is True.
	else:
		# do this if condition1 is True and condition2 is False.
else:
	if condition3:
		# do this if condition1 is False and condition3 is True.
	else:
		# do this if condition1 is False and condition3 is False.
# continue statements. these after statements will run as usually.

NOTE: Give indentation bcoz it defines the block scope of the respective statements.

#------------------------------------------------------------------------------------------------------------
'''

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
	print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
	print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
	print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
	print(f"Your BMI is {bmi}, you are obese.")
else:
	print(f"Your BMI is {bmi}, you are clinically obese.")