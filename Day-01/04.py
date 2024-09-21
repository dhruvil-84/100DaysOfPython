# input() method returns only String values.
a = input("a:")
b = input("b:")

# method1: (swapping while a and b are strings)
a, b = b, a
print("a = " + a)
print("b = " + b)

# method2: (swapping while a and b are strings)
temp = a
a = b
b = temp
print("a = " + a)
print("b = " + b)

#method3: (swapping while a and b are integers)
a = int(a) # Typecasting
b = int(b)
a = a + b
b = a - b
a = a - b
# when a and b are Integers don't use string concatenation(+) while printing those variable values; instead use commas(,).
print("a =", a)
print("b =", b)

# NOTE: comma(,) will print for all type of variables but in string concatenation(+) only string variables will printed.