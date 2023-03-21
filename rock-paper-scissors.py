import random

choices = ["rock", "paper", "scissors"]

def play():
    user_choice = input("Enter your choice: rock, paper or scissors? ").lower()
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        return "It's a tie!"

    if is_win(user_choice, computer_choice):
        return "You won!"

    return "You lost!"

def is_win(player, opponent):
    if (player == "rock" and opponent == "scissors") or (player == "scissors" and opponent == "paper") or (player == "paper" and opponent == "rock"):
        return True

print(play())

