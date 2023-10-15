from art import logo, vs
from game_data import data
from random import randint
from os import system

if __name__ == "__main__":
    incorrect = False
    score = 0
    print(logo)
    while not incorrect:
        profile_a = data[randint(0, 50)]
        profile_b = data[randint(0, 50)]
        print(f"Compare A: {profile_a['name']}, a {profile_a['description']}, from {profile_a['country']}.")
        print(vs)
        print(f"Against B: {profile_b['name']}, a {profile_b['description']}, from {profile_b['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B': ")
        system('clear')
        print(logo)
        if answer == "A":
            if profile_a['follower_count'] > profile_b['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                incorrect = True
        elif answer == "B":
            if profile_a['follower_count'] < profile_b['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                incorrect = True
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            incorrect = True
