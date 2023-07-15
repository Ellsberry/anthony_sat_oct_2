""" This game randomly selects a text string and has players guess the letters in the string"""

import random
import pygame
import pandas


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
    active_player = starting_player(player_score, number_of_players, )

    letters_guessed = []                             # this will be a list of all guessed letters during a single round
    letter_to_be_guessed = find_letters(text_to_be_solved) # this is the text string changed to a list of its characters
    print(text_to_be_solved)
    spaces = text_to_be_solved.count(" ")
    number_of_letters_in_text = len(text_to_be_solved) - spaces
    partially_solved_text = []                   # partially_solved_text is list of characters as the text is filled in

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
        elif guess not in letter_to_be_guessed and guess in ["a", "e", "i", "o", "u"]:
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
    """transform the text_to_be_solved string  to a list of characters"""
    # SINCE THE FUNCTION IS ONE LINE AND ONLY SHOWS UP IN 1 PLACE IN THE GAME REPLACE FIND_LETTERS WITH THIS LIST COMPREHENSION
    letters_to_be_guessed = [text_to_be_solved[index] for index in range(len(text_to_be_solved))]
    return letters_to_be_guessed


def starting_player(number_of_players, name_score):
    """Set active player to lowest player number with highest score"""

    """change player_score to name_score_list in calling parameters
          
       This function needs to be updated to handle 1 to 3 players.
       We need to create a file that contains the player names and scores.
       We need create and call a function named 'read_previous_scores(name_score)' to read the file.
       See the function 'read_previous_scores' below. """


    """Set active player to the lowest player number with the highest score"""
    all_players_scores = read_file("wheel_of_fortune_player_scores.csv")
    all_players_scores = sorted(all_players_scores, key=lambda x: (x[0], x[1]))
    print(all_players_scores)
    print(all_players_scores[0][1])
    z = int(len(all_players_scores))
    for i in range(number_of_players):
        for x in range(z):
            print("line 102: x =  ", x)




    if number_of_players == 1:
        active_player = 0
    # elif number_of_players == 2 and player_highscore[0] >= player_highscore[1]:
    #     active_player = 0
    # elif number_of_players == 2 and player_highscore[0] < player_highscore[1]:
    #     active_player = 1
    # elif player_highscore[0] >= player_highscore[1] and player_highscore[0] >= player_highscore[2]:
    #     active_player = 0
    # elif player_highscore[1] >= player_highscore[2]:
    #     active_player = 1 can u c ths
    else:
        player0 = name_score[0][0]
        if player0 in all_players_scores:
            print(player0)
        else:
            exit()
    # active_player = 0
    return active_player


def read_previous_scores(name_score, number_of_players):
    """Read the previous scores from a file and return a list of lists"""
    """The file previous_scores will be read into a data frame.   
       The data frame will be sorted by player and player score.
       name_score will be returned with the highest previous score"""
    data_frame = pandas.read_csv("wheel_of_fortune_player_scores.csv")
    data_frame.sort_values(by=["name", "score"], ascending=[True, False], inplace=True)
    data_frame = data_frame.reset_index()
    print(data_frame)
    print(name_score)
    for j in range(number_of_players):
        player = name_score[0][j]
        number_of_rows = int(len(data_frame["name"]))
        for i in range(number_of_rows):
            print(f"Name: {data_frame['name'][i]}  Score: {data_frame['score'][i]}")
            print("Index:  ", i)

            if player == data_frame["name"][i]:
                print(f"Name: {data_frame['name'][i]}  Score: {data_frame['score'][i]}")
                print("Index:  ", i)
                print(data_frame["score"][i])
                name_score[2][j] = data_frame["score"][i]
                break
            else:
                print("My favorite number is orange")
    print(name_score)
    highscore_index = name_score.index(name_score[-1])
    name_score = [list(item) for item in zip(*sorted(zip(*name_score), key=lambda x: x[highscore_index], reverse=True))]
    print(name_score)
    return name_score


def process_letter(new_letter, partially_solved_text, solution):
    """Set up new partial_solved_text if this is the first time the function is called
                else add a letter to the partial_solved_text"""

    if len(partially_solved_text) < 1:
        temp_partially_solved_text = ["?" if solution[index] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" else solution[index] for index in range(len(solution))  ]
        partially_solved_text = ""
        for letter in temp_partially_solved_text:
            partially_solved_text += letter

        print('created line 143  ', solution, "  xxx   ", partially_solved_text)

    else:
        temp_partially_solved_text = [new_letter if solution[index] == new_letter else partially_solved_text[index] for index in range(len(solution))]
        partially_solved_text = ""
        for letter in temp_partially_solved_text:
            partially_solved_text += letter

    if partially_solved_text == solution:
        continue_solving_text = False
    else:
        continue_solving_text = True
    # return_list = [continue_solving_text, partially_solved_text, solution]
    return continue_solving_text, partially_solved_text, solution
