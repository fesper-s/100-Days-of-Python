from random import choice
from art import logo
from os import system

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card

def calculate_score(cards):
    if len(cards) == 2 and 11 in cards and 10 in cards:
        return 0
    if 11 in cards and 21 < sum(cards):
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's a draw!")
    elif computer_score == 0:
        print("Computer has a blackjack! You lose!")
    elif user_score == 0:
        print("You have a blackjack! You win!")
    elif 21 < user_score:
        print(f"You scored {user_score}. You lose!")
    elif 21 < computer_score:
        print(f"Computer scored {computer_score}. You Win!")
    else:
        print(f"You scored {user_score} and the computer scored {computer_score}!")
        if (user_score > computer_score):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    while True:
        user_cards = []
        computer_cards = []
        user_score = 0
        computer_score = 0
        print(logo)
        for i in range(4):
            if i < 2:
                user_cards.append(deal_card())
            else:
                computer_cards.append(deal_card())
        while True:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            if (user_score == 0 or computer_score == 0):
                print(f"BlackJack!")
                break
            elif 21 < user_score:
                break
            print(f"Your cards: {user_cards}")
            print(f"Your score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if input("Wants to draw another card? 'y' or 'n': ") == "y":
                user_cards.append(deal_card())
            else:
                break
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        print(f"You final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        compare(user_score, computer_score)
        if input("Wants to play again? 'y' or 'n': ") == "y":
            system("clear")
        else:
            break
