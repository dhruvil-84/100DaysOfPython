"""
Syntax of a class:
    class ClassName:
NOTE: class name must be in PascalCase for a good practice.

PascalCase --> this is a pascal case.
camelCase  --> this is a camel case.
snake_case --> this is a snake case.

In python Data members are known as attributes. (attribute are the things that an object has).
In python member functions are known as methods. (methods are the things that an object does).

"""

# class User:
#     def __init__(self): #python constructor also known as initialise attribute.
#         print("new user being created...")

# user_1 = User()
# user_1.username = "Dhruvil"
# user_1.roll_no = "001"
# print(user_1.username)
# print(user_1.roll_no)

# user_2 = User()
# user_2.username = "galeon"
# user_2.roll_no = "002"
# print(user_2.username)
# print(user_2.roll_no)

class User:
    def __init__(self, roll_no, name): #python constructor also known as initialise attribute.
        print("new user being created...")
        self.roll_no = roll_no # 'self' is like 'this' keyword of java.
        self.username = name
        self.followers = 0
        self.following = 0

    # methods must always have self keyword as their first parameter.
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Dhruvil")
user_2 = User("002", "galeon")
print(user_1.username) # Dhruvil
print(user_1.roll_no) # 001
print(user_2.username) # galeon
print(user_2.roll_no) # 002

print(user_1.followers) # 0
print(user_1.following) # 0
print(user_2.followers) # 0
print(user_2.following) # 0
user_1.follow(user_2)
print(user_1.followers) # 0
print(user_1.following) # 1
print(user_2.followers) # 1
print(user_2.following) # 0
