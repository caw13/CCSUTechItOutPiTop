# Basic text based hangman game
# Created for CCSU Tech It Out camp

import random

def pick_a_word():
    words_file = "hangman_words.txt"
    try:
        f = open(words_file)
        words = f.read().splitlines()
        print(words)
        random.shuffle(words)
        print(words)
        word = words[0]
        f.close()
        return word
    except IOError:
        print("Cannot find the file: %s" % words_file)
    word = input("Enter word for opponent to guess:  ")

def init_game():
    global won
    global guessed_letters
    global lives_remaining
    global word
    guessed_letters = (" ")
    won = False
    word = pick_a_word()
    lives_remaining = 6
    #print(word)

def get_guess():
    guess = input("guess a letter or the word: ")
    print("guess: " + guess)
    check_guess(guess)

def output_current_known():
    global guessed_letters, word
    if len(guessed_letters) > 0:
        print("guessed letters: "+guessed_letters)
    output_word = ""
    for letter in word:
        if guessed_letters.find(letter) >= 0:
            output_word += letter + " "
        else:
            output_word += "_ "
    print(output_word)

def draw_man():
    global lives_remaining
    print("\n\n\n\n")
    if lives_remaining < 6:
        print(" O")
    if lives_remaining == 4:
        print(" | ")
    if lives_remaining == 3:
        print("/|")
    if lives_remaining <= 2:
        print("/|\\")
    if lives_remaining == 1:
        print("/")
    if lives_remaining == 0:
        print("/ \\")


def check_guess(guess):
    if len(guess) == 1:
        check_letter(guess)
    elif len(guess) > 1:
        check_word(guess)
    else:
        print("Invalid guess, try again")


def check_letter(guess):
    global word, guessed_letters, lives_remaining
    if (word.find(guess) > -1):
        print("contains letter!")
    else:
        print("incorrect")
        lives_remaining -= 1
    if len(guessed_letters) == 0:
        guessed_letters = (guess)
    else:
        guessed_letters += guess
    check_if_won()

def check_word(guess):
    global won, lives_remaining
    if (word == guess):
        print("you guessed the word!!!")
        won = True
    else:
        print("incorrect")
        lives_remaining -= 1

def check_if_won():
    global word, guessed_letters, won
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return
    print("You guessed all the letters!")
    won = True

def you_win():
    global word
    print("You won!  You discovered the word was '"+word+"'")

def run_game():
    global lives_remaining, won, word
    while True:
        while lives_remaining > 0 and not won:
            output_current_known()
            get_guess()
            draw_man()
        if won:
            print("You won!  You discovered the word was '"+word+"'")
        else:
            print("You person was hung, sad state :(")
            print("The word was '"+word+"'")
        print("\n\n\n")
        init_game()

init_game()
run_game()
print("THE END")
