import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
	if choice == 0:
		print(rock)
		break
	elif choice == 1:
		print(paper)
		break
	elif choice == 2:
		print(scissors)
		break
	else:
		choice = int(input("Bad input. Please insert a valid value!\n"))
print("Computer chose:")
com_choice = random.randint(0, 2)
if com_choice == 0:
	print(rock)
elif com_choice == 1:
	print(paper)
elif com_choice == 2:
	print(scissors)
if choice == com_choice:
	print("It's a draw")
elif (choice == 0 and com_choice == 1) or (choice == 1 and com_choice == 2) or (choice == 2 and com_choice == 0):
	print("You lose")
elif (choice == 0 and com_choice == 2) or (choice == 1 and com_choice == 0) or (choice == 2 and com_choice == 1):
	print("You win!")
