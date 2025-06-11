import random
from art import logo

def compare(guess, answer):
    if guess > answer:
        return False, "Too high"
    elif answer > guess:
        return False, "Too low."
    else:
        return True, f"You got it! The answer was {answer}"

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    game_over = False
    number = random.randint(1, 100)
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if choice == 'easy':
        attempts = 10
    elif choice == 'hard':
        attempts = 5
    else:
        print("Wrong difficulty, only type 'easy' or 'hard'")

    while not game_over:
        print(f"You have {attempts} attempts remaining to guess the number.")
        u_guess = int(input("Make a guess: "))
        game_over, result = compare(u_guess, number)
        if game_over == False:
            attempts -= 1
        print(result)
        if attempts == 0:
            print("Yor've run out of guesses, you lose.")
            game_over = True
        

while input("Do you want to play a guess game? Type 'Y' or 'N':").lower() == "y":
    print("\n" * 20)
    play_game()
