'''
#------------------------------------------------------------------------------------------------------------

Comparision Operators: (returns boolean values)
1. > 	(Greater than)
2. < 	(Lesser than)
3. >=	(Greater than Equal to)
4. <=	(Lesser than Equal to)
5. ==	(Equals to)
6. !=	(Not Equal to)

NOTE: '=' is an Assignment Operator whereas '==' is an Equals to operator.

#------------------------------------------------------------------------------------------------------------

Shorthand Operators:
1. x += y	(x = x + y)
2. x -= y	(x = x - y)
3. x *= y	(x = x * y)
4. x /= y	(x = x / y)
5. x %= y	(x = x % y)
6. x **= y	(x = x ** y)
7. x //= y	(x = x // y)

#------------------------------------------------------------------------------------------------------------

if statement:

if condition1:
	# do this if condition1 is True. 
if condition2:
	# do this if condition2 is True. (independent of condition1)
if condition3:
	# do this if condition3 is True. (independent of condition1 and condition2)
# continue statements. these "after statements" will run as usually.

#------------------------------------------------------------------------------------------------------------

if..else statements:

if condition:
	# do this if condition is True.
else:
	# do this if condition is False.
# continue statements. these "after statements"" will run as usually.

NOTE: Give indentation bcoz it defines the block scope of the respective statements.

#------------------------------------------------------------------------------------------------------------
'''

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
	print(f"{number} is EVEN")
else:
	print(f"{number} is ODD")