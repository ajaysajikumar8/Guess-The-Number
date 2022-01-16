#Number Guessing Game Objectives:
import random
from art import logo
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.

def easy():
    return 10

def hard():
    return 5

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        turns = easy()
    else:
        turns = hard()
    actual_answer = random.choice(range(101))
    game_over = False
    while not game_over:
        if turns != 0:
            print(f"You have {turns} attempts remaining to guess the number.")
            user_input = int(input("Make a guess: "))
            if user_input > actual_answer:
                print("Too high")
                turns -= 1 
            elif user_input == actual_answer:
                print("Correct Guess")
                game_over = True
            else:
                print("Too low")
                turns -= 1 
        else:
            print("You've run out of guesses, You lose")
            game_over = True
    choice = input("Do you want to play again? Type 'y' for yes and 'n' for no. ")
    if choice == "y":
        game()

game()
    


    


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

