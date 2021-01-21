"""
100 days of Python course
DAY 7
"""

# please ensure the art and words modules, supplied in this repository
# are in the same place where you run this one from
# they contain ASCII art and a word list and can be viewed in notepad
import random
from hangman_art import stages, logo
from hangman_words import word_list

# note that code produced in spyder shows error:
# from replit import clear

# the logo is in the imported module called hangman_art
print(logo)

# boolean operation to see if game still in progress and a counter for lives
game_is_finished = False
lives = len(stages) - 1

# the word_list is from the imported module called hangman_words
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# this in range loop makes the underscores to show the blank "letters"
display = []
for _ in range(word_length):
    display += "_"

# while loop keeps program active: it will stay active until boolean condition met
while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    # Use the clear() function imported from replit to clear the output between guesses.
    # clear()
    # note above commented out so the screen will not be cleared in spyder environment

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
