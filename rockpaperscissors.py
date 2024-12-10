Rock
import os
import random

def get_choice():
    print ("Enter your choice (Rock, Paper, Scissors) ")
    player_choice = input()
    options = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(options)
    choices = {"Player": player_choice, "Computer": computer_choice}
    print (f"player choice is {player_choice}, computer choice is {computer_choice}")
    return choices

def check_outcome(player, computer):
    if player == computer:
        return "It is a tie !!"
    elif player == "Rock":
        if computer == "Scissors":
            return "Rock breaks the Scissors! You WIN!!"
        else:
            return "Paper covers the Rock! You LOSE"
    elif player == "Paper":
        if computer == "Rock":
            return "Paper covers the Rock! You WIN!!"
        else:
            return "Scissors cut the Paper! You LOSE"
    elif player == "Scissors":
        if computer == "Paper":
            return "Scissors cuts the Paper! You WIN"
        else:
            return "Rock breaks teh scissors! You LOSE"

choices = get_choice()
print (check_outcome(choices["Player"], choices["Computer"]))