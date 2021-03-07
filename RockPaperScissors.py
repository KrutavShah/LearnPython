#Created by Krutav Shah. (C) 2021 All Rights Reserved.
import time
import random

choices = ["rock", "paper", "scissors"]
print("Created by Krutav Shah. (C) 2021 All Rights Reserved.")
print("Welcome to Rock Paper Scissors Game!")

while True:
    print("\nChoices: 1. rock, 2. paper, 3. scissors.")
    human = input("Pick your weapon: ")
    user = human.lower()
    print("Thank you.")
    time.sleep(0.3)
    print("System is picking their weapon. Revealing in 3 seconds.")
    time.sleep(3)
    system = random.choice(choices)
    print(f"\nYou chose {user} and the computer chose {system}.\n")
    
    if user == system:
        print(f"Both players selected {user}. It's a tie.")
    elif user == "rock":
        if system == "scissors":
            print("Rock smashes scissors, so you win!")
        else:
            print("Paper covers rock, so you lose.")
    elif user == "paper":
        if system == "rock":
            print("Paper covers rock, so you win!")
        else:
            print("Scissors cuts paper, so you lose.")
    elif user == "scissors":
        if system == "paper":
            print("Scissors cuts paper, so you win!")
        else:
            print("Rock smashes scissors, so you lose.")

    repeat = input("\nDo you want to play again? (yes/no): ")
    if repeat.lower() != "yes":
        break 