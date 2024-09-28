def prime_checker(number):
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    if number == 1 or number == 0:
        print(f"{number} is neither prime nor co-prime.")
    elif flag == False or number < 0:
        print(f"The number {number} is not prime.")
    else:
        print(f"The number {number} is prime.")

n = int(input("Check this number: "))
prime_checker(number = n)