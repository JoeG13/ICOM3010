# rock, paper, scissors game: Simple implementation of the game
import random

def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
play_game(user_choice)
