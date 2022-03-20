""" This game randomly selects a text string and has players guess the letters in the string"""

import random
import pygame


def main():
    game_loop()


def game_loop():
    """Solve one or more text problems"""
    # initialize game variables
    active_player, continue_running_game, continue_solving_text, letters_in_alphabet, number_of_players, player, player_score, rewards_list, text_list = initialize()
    # Randomly select text to be solved
    text_to_be_solved = choose_item(text_list).lower()
    player_loop(text_to_be_solved, active_player, continue_running_game, continue_solving_text, letters_in_alphabet, number_of_players, player, player_score, rewards_list, text_list)
    print("scores")
    if input("Continue Playing Game y or n:  ") == "n":
        quit()


# Initialize variables at start of game
def initialize():
    continue_running_game = True
    continue_solving_text = True
    number_of_players = 0
    player = []
    player_score = []
    letters_in_alphabet = "abcdefghijklmnopqrstuvwxyz"
    text_list = read_file("Animals_1.txt")
    rewards_list = read_file("wheel_of_fortune_rewards.txt")
    # Determine the number of players and their names
    number_of_players = input("Enter the number of players:  ")
    number_of_players = int(number_of_players)
    player = [input(f"Enter the name of player number {index + 1}:   ") for index in range(number_of_players)]
    print(player)
    player_score = [0 for index in range(number_of_players)]
    print(player_score)
    active_player = 0
    return active_player, continue_running_game, continue_solving_text, letters_in_alphabet, number_of_players, player, player_score, rewards_list, text_list


def read_file(filename) -> list:
    """ generic read file function - will output a list containing each line in the specified file"""
    with open(filename) as stuff:
        return [line.rstrip("\n") for line in stuff.readlines()]


def choose_item(item_list) -> str:
    """Randomly select an element from a file"""
    item = random.choice(item_list)
    return item

def player_loop(text_to_be_solved, active_player, continue_running_game, continue_solving_text, letters_in_alphabet, number_of_players, player, player_score, rewards_list, text_list):
    """ Loop through 1 to 3 players until game problem is solved
     each player gets to guess a new letter or vowel
     if the text includes the letter the player gets another turn"""

    # determine which player starts the game round.
    active_player = starting_player(player_score, number_of_players)

    letters_guessed = []                             # this will be a list of all guessed letters during a single round
    letter_to_be_guessed = find_letters(text_to_be_solved)  # this is the text string changed to a list of its characters
    print(text_to_be_solved)
    spaces = text_to_be_solved.count(" ")
    number_of_letters_in_text = len(text_to_be_solved) - spaces
    partially_solved_text = []                      # partially_solved_text is list of characters as the text is filled in

    guess = " "

    while continue_solving_text:
        # Show the text and a picture on a game board and get players guess
        # for now all displays are sent to Python Console
        print(process_letter(guess, partially_solved_text, letter_to_be_guessed))
        # select a reward or penalty
        reward = int(choose_item(rewards_list))

        if active_player >= number_of_players:
            active_player = 0

        # input a players guess
        print(f"The hidden text has {number_of_letters_in_text} letters and {spaces} spaces.")
        guess = input(
            f"{player[active_player]}'s score is: {player_score[active_player]}.  Reward for correct letter is {reward}.  Input a letter:  ")

        if guess not in letters_in_alphabet:
            print("input not a letter")
            player_score[active_player] -= reward
            active_player += 1
            break
        elif guess in letters_guessed:
            print("Don't be a duffus.  This letter was already guessed!!!")
            player_score[active_player] -= reward
            active_player += 1
            break
        elif guess not in letter_to_be_guessed and guess in ["aeiou"]:
            print("Vowel is not in text")
            player_score[active_player] -= 250
            active_player += 1
            break
        elif guess in ["aeiou"] and guess in ["aeiou"]:
            player_score[active_player] -= 250
        else:
            player_score[active_player] += letter_to_be_guessed.count(guess) * reward

        letters_guessed.append(guess)
        continue_solving_text, partially_solved_text, solution = process_letter(guess, partially_solved_text, text_to_be_solved)
        # active_player += 1


def find_letters(text_to_be_solved):
    """transform the text_to_be_solved string  1o a list of characters"""
    # SINCE THE FUNCTION IS ONE LINE AND ONLY SHOWS UP IN 1 PLACE IN THE GAME REPLACE FIND_LETTERS WITH THIS LIST COMPREHENSION
    letters_to_be_guessed = [text_to_be_solved[index] for index in range(len(text_to_be_solved))]
    return letters_to_be_guessed


def starting_player(player_score, number_of_players):
    """Set active player to lowest player number with highest score"""
    if number_of_players == 1:
        active_player = 0
    elif number_of_players == 2 and player_score[0] >= player_score[1]:
        active_player = 0
    elif number_of_players == 2 and player_score[0] < player_score[1]:
        active_player = 1
    elif player_score[0] >= player_score[1] and player_score[0] >= player_score[2]:
        active_player = 0
    elif player_score[1] >= player_score[2]:
        active_player = 1
    else:
        active_player = 2
    return active_player


def process_letter(new_letter, partially_solved_text, solution):
    """Set up new partial_solved_text if this is the first time the function is called
                else add a letter to the partial_solved_texxt"""

    if len(partially_solved_text) < 1:
        partially_solved_text = [" " if solution[index] in "abcdefghijklmnopqrstuvwxyz" else solution[index] for index in range(len(solution))  ]

    partially_solved_text = [new_letter if solution[index] == new_letter else partially_solved_text[index] for index in range(len(solution))]

    if partially_solved_text == solution:
        continue_solving_text = False
    else:
        continue_solving_text = True
    return_list = [continue_solving_text, partially_solved_text, solution]
    return continue_solving_text, partially_solved_text, solution


# Start Game
if __name__ == "__main__":
    main()
