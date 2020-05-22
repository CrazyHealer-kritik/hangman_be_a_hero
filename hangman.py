# -*- coding: utf-8 -*-
"""
Created on Fri May 22 03:02:01 2020

@author: kritik
"""
import random #importing random lib.
from word import word_list #importing my word list with my friends names.
def player():
    name = input("player please enter your name : ")
    print(name + " Let's play a DEATH game called Hangman!")
    story = "Your friend has been kidnapped, and you dont know which of your friend\n kidnapper ngociates with you \"if you can guess the correct name of your friend,\n then he will live him/her or if you failed he/she will be hanged to death \" \n now its your resopnsiblity to save them "
    print(story)
    return name

def get_word():
    word = random.choice(word_list) #choosing one random name from word list
    return word.upper()


def play(word,name):
    word_completion = "-" * len(word) #checking for word length and replacing each letters by "-"
    guessed = False #initial no gassed make.
    guessed_letters = [] #list of all guessed letters that user made while playing
    guessed_words = [] #if the player  guessed the whole word that word will store here.
    tries = 6 #total tries player have.
    
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats,"+name+" you saved "+word+"! You win!")
    else:
        print("Sorry, " + name +" you ran out of tries. you let your friend " + word + "dies. Maybe next time you can save your friends!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    name = ""
    player()
    word = get_word()
    play(word,name)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word,name)


if __name__ == "__main__":
    main()
