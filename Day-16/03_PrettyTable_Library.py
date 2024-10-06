# about pretty table library - code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

from prettytable import *
table = PrettyTable()
print(table)
print(type(table))
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"], "l")
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"], "l")
print(table)
table.align = "c"
print(table.align)
print(table)