'''
----------------------------------------- SCOPE -----------------------------------------

--> Scope refers to the area of a program where a variable is accessible.
--> Python has 4 levels of scope, often abbreviated as LEGB (Local, Enclosing, Global, Built-in).
--> There is no concept of Block Scope in Python.

-------------------------------------- GLOBAL SCOPE -------------------------------------

--> A variable declared outside all functions and classes is in the global scope.
--> It is accessible anywhere in the script, including inside functions (unless shadowed by a local variable).
--> Global variables persist for the entire life of the program.

------------------------------------- LOCAL SCOPE ---------------------------------------

--> A variable declared inside a function is in the local scope.
--> It is only accessible within that function.
--> Local variables are destroyed once the function execution is completed.
--> If you try to access a local variable outside the function, you will get a NameError.

--------------------- How to access Global variable in Local scope? ---------------------

--> If a local variable and a global variable share the same name, the local variable shadows the global variable inside the function.
--> The global variable remains unchanged unless the global keyword is used.

--> Inside a function, to modify/access a global variable, you must declare it using the global keyword.
--> This allows you to change the value of a global variable from (local scope)within a function.

------------------------------------- BEST PRACTICES ------------------------------------

--> Use local variables for values that are only needed within a function.
--> Minimize the use of global variables for cleaner, modular, and maintainable code.
--> If global variables are necessary, use the global keyword sparingly and clearly comment on its use.
--> use return keyword and return the updated value if you want to modify the global scope.

-----------------------------------------------------------------------------------------

'''

PI = 3.1415

def access():
    print(PI) # Output: 3.1415

access()
print(PI)  # Output: 3.1415

#-----------------------------------------------------------------

x = 5

def modify_global():
    global x  # Tells Python to use the global variable
    x = 10

modify_global()
print(x)  # Output: 10

#-----------------------------------------------------------------

y = 50  # Global variable

def test():
    y = 100  # Local variable shadows the global one
    print(y)  # Prints 100 (local variable)

test()
print(y)  # Prints 50 (global variable remains unchanged)

#-----------------------------------------------------------------

z = 7  # Global variable

def demo():
    z = 10  # Local variable (shadows global z)
    print(f"local z is {z}")   # Accesses local variable
    print(f"global z is {globals()['z']}")  # Accesses the global variable using globals()

#def demo():
#    global z
#    print(f"local x is {z}")
#    print(f"global x is {z}")

demo()

#-----------------------------------------------------------------
