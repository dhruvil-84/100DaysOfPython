class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("inhale, exhale....")

# Non - Inherited.
# class fish:
#     def swim(self):
#         print("moving in water.")

# Inherited.
class Fish(Animal): # class fish extends class Animal.
    def __init__(self):
        super().__init__() # executing parent's constructor in child's so when child object is created, parent properties also inherits.

    def swim(self):
        print("moving in water.")

    def breathe(self): # method overriding.
        super().breathe()
        print("under the water..")

nemo = Fish()
print(nemo.num_of_eyes)
nemo.swim()
nemo.breathe()

# we will use concept of inheritance in Snake game by inheriting our snake class from turtle class and add some extra methods in it.