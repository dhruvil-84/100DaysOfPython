# 123_456_789 is treated as same as 123456789. Just bcoz we can't put commas like 123,456,789 for readibility python gives us Underscores.

two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))