import random
from hangman_art import stages, logo
from hangman_word import word_list

chosen_word = random.choice(word_list)
lives = 6

print(logo)
print(f"Pssst, the solution is {chosen_word}")

display = []
for char in chosen_word:
	display.append("_")

while True:
	guess = input("Guess a letter: ").lower()
	if guess in display:
		print(f"You've already guessed {guess}")
	if not guess in chosen_word:
		lives -= 1
		print(f"You guessed {guess}, that's not in the word. You lose a life.")
	else:
		for position in range(len(chosen_word)):
			char = chosen_word[position]
			if char == guess:
				display[position] = char

	print(f" ".join(display))
	print(stages[lives])

	if lives == 0:
		print("You lose.")
		break
	if "_" not in display:
		print("You win!")
		break
