line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")

if position[0] == "A":
	columns = 0
elif position[0] == "B":
	columns = 1
elif position[0] == "C":
	columns = 2
row = int(position[1]) - 1
map[row][columns] = "X" 

print(f"{line1}\n{line2}\n{line3}")
