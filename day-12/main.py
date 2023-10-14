from random import randint

def set_difficulty():
    global attempts
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while True:
        if difficulty == "easy":
            attempts = 10
            break
        elif difficulty == "hard":
            attempts = 5
            break
        else:
            difficulty = input("Choose a valid input. Type 'easy' or 'hard': ")
    return difficulty

def guessing_game(attempts, number):
    run_out_attempts = False
    correct = False
    while not run_out_attempts and not correct:
        print(f"You have {attempts} attempts remaing to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.\nGuess again.")
        elif guess < number:
            print("Too low.\nGuess again")
        elif guess == number:
            print(f"You got it! The answer was {number}")
            correct = True
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            run_out_attempts = True

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    attempts = 0
    difficulty = set_difficulty()
    guessing_game(attempts, number)
