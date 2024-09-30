def is_leap(year):
    """Takes the year number and returns True if its a Leap year, otherwise returns False."""
    # The above line is a Docstring used for documentation of functions, It gives each function a little bit of an explainer.
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

def days_in_month(year, month):
    """Takes the year and month number and return total number of days in that valid month. If month is not valid then it returns -1."""
    # The above line is a Docstring used for documentation of functions, It gives each function a little bit of an explainer.
    if is_leap(year):
        month_days = [31, 29 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_days = [31, 28 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month >= 1 and month <= 12:
        return month_days[month - 1]
    else:
        return -1

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)