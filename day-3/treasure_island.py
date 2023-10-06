print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
print("Welcome to Treasure Island.\nYour Mission is to find the treasure.\n")

choice = input("You are in a dungeon, and you are seeing two doors, the 'left' door and the 'right' door. Wich do you choose? ").lower()
if choice == "left":
	choice = input("You open it and enter the room. You have fall into a pool. You choose to 'swim' or to 'wait'? ").lower()
	if choice == "wait":
		choice = input("You wait.......... AND! 3 different doors just have appeard. Which one you choose, the 'red' one, the 'blue' one or the 'yellow' one? ").lower()
		if choice == "red":
			print("You open it and a dragon spit flames on you.\nGame Over")
		elif choice == "blue":
			print("You open it, and a couple of starving beasts jump in your direction.\nGame Over.")
		elif choice == "yellow":
			print("You have found it!\nYou Win!")
		else:
			print("You stupid! You are drowned!\nGame Over.")
	else:
		print("Somehow you are attacked by a trout.\nGame Over.")
else:
	print("Somehow you have fall into a hole.\nGame Over.")
