from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check user's check against actual answer
def check_answer(guess, answer, turns):
    """Checks answer against guess and returns the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1 
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

#make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"The correct answer is {answer}")

    #let the user guess a number

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number. ")

    #Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)


game()

#track the number of turns and reduce by 1 if they get it wrong


