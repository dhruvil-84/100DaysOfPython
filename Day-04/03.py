row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

if (int(position[0]) - 1 >= len(map)) or (int(position[0]) - 1 < 0) or (int(position[1]) - 1 >= len(map)) or (int(position[1]) - 1 < 0):
	print("Invalid Coordinates")
else:
	map[int(position[0]) - 1][int(position[1]) - 1] = 'X'
	print(f"{row1}\n{row2}\n{row3}")