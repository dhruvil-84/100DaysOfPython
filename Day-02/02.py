'''
Arithmetic Operators:
1. Addition         (x + y)
2. Subraction       (x - y)
3. Multiplication   (x * y)
4. Division         (x / y)  --> Always returns float value. (Implicit Type conversion happens into float when in an expression).
5. Modulus          (x % y)
6. Exponentiation   (x ** y)
7. Floor Division   (x // y)
'''

height = eval(input("enter your height in m: ")) # input() always returns into str data type so explicit type casting is done.
weight = eval(input("enter your weight in kg: ")) # input() always returns into str data type so explicit type casting is done.
print(int(weight / height ** 2))