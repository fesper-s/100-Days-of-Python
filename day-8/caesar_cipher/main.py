from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
	cipher_text = ""
	for char in text:
		if char in alphabet:
			position = alphabet.index(char)
			if direction == "encode":
				position += shift
				if position >= len(alphabet):
					position -= len(alphabet)
			elif direction == "decode":
				position -= shift
				if position < 0:
					position += 26
			cipher_text += alphabet[position]
		else:
			cipher_text += char
	print(f"Here's the {direction}d result: {cipher_text}")

print(logo)
repeat = "yes"
while repeat == "yes":
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	shift %= 26
	caesar(text, shift, direction)
	repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
print("Goodbye")
