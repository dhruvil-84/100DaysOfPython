'''
Positional Arguments VS Keyword Arguments.
'''

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

# Positional Arguments.
print("Using Positional Arguments: ")
print("1.")
nameAge("Prince", 20)
print("2.")
nameAge(20, "Prince")

# Keyword Arguments.
print("\nUsing Keyword Arguments: ")
print("1.")
nameAge(name = "Prince", age = 20)
print("2.")
nameAge(age = 20, name = "Prince")