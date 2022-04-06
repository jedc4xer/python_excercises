import requests
import random
import string
import os
import time

# Clean the screen
os.system("cls")

# Provide a mock option, then populate and display choice
input("Choose a difficulty. (easy, medium, hard) >> ")
os.system("cls")
print("Choose a difficulty. (easy, medium, hard) >> extreme")
print("Extreme Difficulty Chosen\n")
print(
    "You are restricted from seeing which letters or words you have tried. GOOD LUCK! \n"
)

# Display program status prior to potential longer-running task
print("Please Wait... \nAccessing Word List... This may take a moment....\n")

# Get txt file from web
file = requests.get(
    "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
)

# Prepare file for use and display filtering choices used
words = set(file.text.replace("\n", "").split("\r"))
limited_words = [_ for _ in words if len(_) >= 7]
print(
    f'{"{:,}".format(len(words))} words found - Limiting to {"{:,}".format(len(limited_words))} words with 7 or more characters.\n\n'
)

# ************** FUNCTIONS *********************
def pick_random_word():
    random_word = random.choice(limited_words)
    return random_word


def collect_guess():
    # Start Guess Loop
    passed = False
    while not passed:
        print("\n", "***** RUNTIME OPTIONS *****")
        print('1. "exit game" | Exit the game', "\n")

        # Take user input
        guess = input("Type your guess of a word or letter. >> ")

        # Check for exit command
        if guess == "1" or guess.lower() == "exit game":
            print("Thank you for playing!", "\n")
            quit()

        # Clean guess for program usage
        cleaned_guess = "".join(_ for _ in guess if _ in string.ascii_letters)

        # Check for validity and catch errors
        try:
            if len(cleaned_guess) < 1:
                raise ValueError

            cleaned_guess = cleaned_guess.lower()
            passed = True
        except:
            print("**************************************************")
            print(
                f'You entered "{guess}". This is invalid, you must guess a word or letter.'
            )
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    return cleaned_guess


def display_guess_status(random_word, guesses, clean_screen):
    guessed_string = ""
    for char in random_word:
        if clean_screen == "clean":
            os.system("cls")
            guessed_string += char if char in guesses else "_"
            display_string = guessed_string + "*" * (
                len(random_word) - len(guessed_string)
            )
        elif clean_screen == "game_over":
            guessed_string += char if char in guesses else "_"
            display_string = guessed_string + "*" * (
                len(random_word) - len(guessed_string)
            )
        else:
            guessed_string += "*"
            display_string = guessed_string

        print(
            "\n", "######## WORD GUESSING GAME ########"
        ) if clean_screen == "clean" else None
        print("\n    ", display_string)
        time.sleep(0.2)
    if clean_screen:
        os.system("cls")

    guess_status = f"  |  {len(''.join(_ for _ in random_word if _ in guesses))} out of {len(random_word)} characters guessed."
    print("\n", "######## WORD GUESSING GAME ########")
    print("\n    ", display_string, guess_status)

# ************ End Declared Functions *******************

random_word = pick_random_word()

# Assign Primary Variables
available_guesses = 7
game_won_printout = "Congratulations! You got it correct!"
game_lost_printout = "Sorry! You have lost the game this time.\n\n Better luck next time!!"
guess_result = ""
guess_count = 0

# Set first-run rule
clean_screen = False

# Create list for guesses (does not need to be a set)
guesses = []

# Game Loop
game_over = False
while not game_over:
    display_guess_status(random_word, guesses, clean_screen)
    print("\n", guess_result)
    print(f"You have {available_guesses} attempts left.")
    clean_screen = "clean"
    cleaned_guess = collect_guess()
    guess_count += 1
    
    # Logic if the length of the guess is more than a single letter
    if len(cleaned_guess) >= 2:
        if cleaned_guess == random_word.lower():
            os.system("cls")
            print(game_won_printout)
            game_over = True
            status = "WINNER "
        else:
            if available_guesses > 2:
                available_guesses -= 2
                guess_result = f"Oops!!! You did not get that correct. You just lost 2 guesses and have {available_guesses} remaining."
            else:
                os.system("cls")
                print(game_lost_printout)
                game_over = True
                status = "LOSER "
                
    # Logic if the length of the guess indicates a single letter
    else:
        
        # Logic if the single letter is in the word
        if cleaned_guess in random_word.lower():
            if cleaned_guess in guesses:
                guess_result = (
                    "Oops, while that letter is an option... You already picked it!!"
                )
            else:
                guess_result = f"Congratulations! You found a match. You have {available_guesses} guesses remaining."
            guesses.append(cleaned_guess)
            for letter in random_word.lower():
                if letter not in guesses:
                    game_over = False
                    break
                else:
                    guess_result = game_won_printout
                    game_over = True
                    status = "WINNER "
                    
        # Logic if the single letter is not in the word
        else:
            if available_guesses == 1:
                os.system("cls")
                print(game_lost_printout)
                game_over = True
                status = "LOSER "
            else:
                available_guesses -= 1
                tries_term = "try" if available_guesses == 1 else "tries"
                guess_result = f"Sorry! You did not choose a correct letter. You have {available_guesses} {tries_term} left."
                
# Flood the Screen and display results
# TO INCLUDE - Accuracy Counter
print(status * 100000)
display_guess_status(random_word, guesses, clean_screen="game_over")

print(f"\n{status * 3}\nThe mystery word was {random_word.capitalize()} and your accuracy was {round(len(guesses)/guess_count,2) * 100}%\n{status * 3}\n")
