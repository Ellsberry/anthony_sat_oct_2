""" This game is for up to 3 players.  You will need the locations on your computer
 for the animal pictures and player data """
import sys
import pygame
import os
import time
from Wheel_of_Fortune_using_run_screen import read_file, choose_item, starting_player, find_letters, process_letter

# get the path of the game directory
game_path = os.getcwd()

def main():


    pygame.init()
    clock = pygame.time.Clock()

    # create the over all game surface
    game_surface = game_screen()

    # create the solution text board
    solution_board(game_surface, "Wheel of Fortune")
    pygame.display.flip()
    clock.tick(60)

    # create the initial player surface with 3 players
    name_score = [["bugs", "daffy", "sam"], ["0", "0", "0"], ["0", "0", "0"]]
    player_surface(game_surface, name_score, 0)

    # show game masters of ceremony
    picture = r"C:\Users\Steve Ellsberry\PycharmProjects\anthony_steve_wheel_of_fortune\player_pictures\anthony_steve.jpg"
    # picture = r"C:\Users\ajh08_idy4tts\Documents\anthony_steve_wheel_of_fortune\player_pictures\anthony_steve.jpg"
    clue_surface(picture, game_surface)

    # create input screen and obtain number of players and their names
    input_message(game_surface, 'Enter the number of people playing (1, 2, or 3)?')
    pygame.display.flip()
    number_of_players = get_input("number", game_surface)
    input_message(game_surface, 'Enter name of player number 1')
    pygame.display.flip()
    player_1_name = get_input("string", game_surface)
    name_score[0][0] = player_1_name
    if number_of_players >= 2:
        input_message(game_surface, 'Enter name of player number 2')
        pygame.display.flip()
        player_2_name = get_input("string", game_surface)
        name_score[0][1] = player_2_name
    if number_of_players == 3:
        input_message(game_surface, 'Enter name of player number 3')
        pygame.display.flip()
        player_3_name = get_input("string", game_surface)
        name_score[0][2] = player_3_name
        player_surface(game_surface, name_score, number_of_players)

    continue_running_game = True
    continue_solving_text = True
    player = []
    active_player = 0
    letters_in_alphabet = "abcdefghijklmnopqrstuvwxyz"

    text_list = read_file(game_path + r"\Animals_1.txt")
    rewards_list = read_file(game_path + r"\wheel_of_fortune_rewards.txt")
    text_to_be_solved = choose_item(text_list).lower()
    player_loop(text_to_be_solved, active_player, continue_running_game, continue_solving_text, letters_in_alphabet,
                number_of_players, player, name_score, rewards_list, text_list,game_surface)
    print("scores")
    if input("Continue Playing Game y or n:  ") == "n":
        quit()
    time.sleep(10)


def game_screen():
    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption("Anthony's Animal Wheel of Fortune")
    screen.fill((255, 0, 0))
    pygame.display.flip()
    return screen

#
def solution_board(surface, text):
    """this module shows the text to be solved"""
    font = pygame.font.SysFont("Arial", 80)
    rec = pygame.Rect(20, 20, 1220, 120)
    pygame.draw.rect(surface, (250, 250, 0), rec)
    prompt = font.render(text, False, (0, 0, 250))
    surface.blit(prompt, (60, 40))


def player_surface(surface, name_score, number_of_players=0):
    """ This function displays player information"""
    # Find on your computer the folder location for player pictures.
    # This URL is for Steve's Computer
    player_data_path = r"C:\Users\Steve Ellsberry\PycharmProjects\anthony_steve_wheel_of_fortune\player_pictures"
    # This URL is for Anthony's computer
    # player_data_path = r"C:\Users\ajh08_idy4tts\Documents\anthony_steve_wheel_of_fortune\player_pictures"

    os.chdir(player_data_path)
    x, y = 20, 380
    blank_name_score = [["      ", "      ", "      "], ["   ", "   ", "   "], ["  ", "  ", "  "]]
    font = pygame.font.SysFont("Arial", 30)
    for row in range(3):
        for column in range(number_of_players):
            rec = pygame.Rect(x + 220 * column, y + 40 * row, 300, 40)
            pygame.draw.rect(surface, (0, 0, 0), rec, 0)
            text_surface = font.render(blank_name_score[row][column], False, (0, 255, 0))
            surface.blit(text_surface, ((x + 10) + (320 * column), (y + 10) + (row * 35)))
            pygame.display.flip()

    # display the following pictures if there is no picture for players
    if number_of_players == 0:
        player1_image = pygame.image.load('bugs.jpg')
        player1_image = pygame.transform.scale(player1_image, (200, 200))
        surface.blit(player1_image, (20, 500))
        player2_image = pygame.image.load('daffy.jpg')
        player2_image = pygame.transform.scale(player2_image, (200, 200))
        surface.blit(player2_image, (320, 500))
        player3_image = pygame.image.load('sam.jpg')
        player3_image = pygame.transform.scale(player3_image, (200, 200))
        surface.blit(player3_image, (620, 500))
        pygame.display.flip()

        # display current score.  At the beginning of game scores are 0.
        #      EVENTUALLY THE FOLLOW DATA WILL COME FROM A FILE
        name_score = [["bugs", "daffy", "sam"], ["0", "0", "0"], ["0", "0", "0"]]
    elif number_of_players == 1:
        pass

    # Set up rectangle space for player data
    number_of_players = 3
    x, y = 20, 380
    font = pygame.font.SysFont("Arial", 30)
    for row in range(3):
        for column in range(number_of_players):
            rec = pygame.Rect(x + 220 * column, y + 40 * row, 300, 40)
            pygame.draw.rect(surface, (0, 0, 0), rec, 1)
            text_surface = font.render(name_score[row][column], False, (0, 255, 0))
            surface.blit(text_surface, ((x + 10) + (320 * column), (y + 10) + (row * 35)))
            pygame.display.flip()
    return surface

def player_loop(text_to_be_solved, active_player, continue_running_game, continue_solving_text, letters_in_alphabet, number_of_players, player, name_score, rewards_list, text_list, surface):
    """ Loop through 1 to 3 players until game problem is solved
     each player gets to guess a new letter or vowel
     if the text includes the letter the player gets another turn"""

    # determine which player starts the game round.
    # active_player = starting_player(player_score, number_of_players)
    active_player = 0

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
        printable_partial_text = []
        for i in range(len(text_to_be_solved)):
            printable_partial_text = printable_partial_text + partially_solved_text[i]
        print("line 165", printable_partial_text)
        # solution_board(surface, partially_solved_text)
        print(process_letter(guess, partially_solved_text, letter_to_be_guessed))
        # select a reward or penalty
        reward = int(choose_item(rewards_list))

        if active_player >= number_of_players:
            active_player = 0

        # input a players guess
        print(f"The hidden text has {number_of_letters_in_text} letters and {spaces} spaces.")
        guess = input(
            f"{name_score[0][active_player]}'s score is: {name_score[1][active_player]}.  Reward for correct letter is {reward}.  Input a letter:  ")
        print("line 178 name_score ", name_score)
        print("line 178 name_score ", name_score[1][active_player])
        score = int(name_score[1][active_player])
        if guess not in letters_in_alphabet:
            print("input not a letter")
            score -= reward
            name_score[1][active_player] = str(score)
            active_player += 1
            break
        elif guess in letters_guessed:
            print("Don't be a duffus.  This letter was already guessed!!!")
            score -= reward
            name_score[1][active_player] = str(score)
            active_player += 1
            break
        elif guess not in letter_to_be_guessed and guess in ["aeiou"]:
            print("Vowel is not in text")
            score -= 250
            name_score[1][active_player] = str(score)
            active_player += 1
            break
        elif guess in ["aeiou"] and guess in ["aeiou"]:
            score -= 250
            name_score[1][active_player] = str(score)
        else:
            score += letter_to_be_guessed.count(guess) * reward
            name_score[1][active_player] = str(score)

        letters_guessed.append(guess)
        continue_solving_text, partially_solved_text, solution = process_letter(guess, partially_solved_text, text_to_be_solved)
        # active_player += 1


def clue_surface(clue_file, surface):
    """The clue_surface shows a picture related to the text to be solved"""
    # Find on your computer the folder locations for animal pictures.
    # This URL is for Steve's Computer
    animal_jpgs_path = r"C:\Users\Steve Ellsberry\PycharmProjects\anthony_steve_wheel_of_fortune\image"
    # This URL is for Anthony's computer
    # animal_jpgs_path = r"C:\Users\ajh08_idy4tts\Documents\anthony_steve_wheel_of_fortune\image"

    os.chdir(animal_jpgs_path)
    clue_image = pygame.image.load(clue_file)
    clue_image = pygame.transform.scale(clue_image, (400, 400))
    surface.blit(clue_image, (950, 300))
    pygame.display.flip()


def input_message(surface, text):
    """this module shows the input requests"""
    # blank out any previous user inputs
    font = pygame.font.SysFont("Arial", 40)
    rec = pygame.Rect(20, 210, 1220, 100)
    pygame.draw.rect(surface, (0, 0, 250), rec)
    prompt = font.render(" ", False, (0, 0, 0))
    surface.blit(prompt, (30, 230))
    pygame.display.flip()

    font = pygame.font.SysFont("Arial", 40)
    rec = pygame.Rect(20, 140, 1220, 70)
    pygame.draw.rect(surface, (0, 250, 0), rec)
    prompt = font.render(text, False, (0, 0, 250))
    surface.blit(prompt, (30, 150))
    pygame.display.flip()


def get_input(type_input, surface):
    """get input data that is either a 'number' or a 'string' """
    # create input screen
    font = pygame.font.SysFont("Arial", 40)
    rec = pygame.Rect(20, 210, 1220, 100)
    pygame.draw.rect(surface, (0, 0, 250), rec)
    prompt = font.render(" ", False, (250, 250, 0))
    surface.blit(prompt, (30, 230))
    pygame.display.flip()
    # get input
    user_text = ''
    get_user_input = True
    while get_user_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                break
            if event.type == pygame.KEYUP:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                    print("key shift left:", pygame.K_RSHIFT)
                    break
                if event.unicode.isalnum():
                    user_text += event.unicode
                    pygame.draw.rect(surface, (0, 0, 250), rec)
                    prompt = font.render(user_text, False, (250, 250, 0))
                    surface.blit(prompt, (30, 230))
                    pygame.display.flip()
                else:
                    return user_text

            if type_input == "number":
                if user_text in ['1', '2', '3']:
                    return int(user_text)
                else:
                    user_text = ""
                    break

    time.sleep(25)
    return user_text[:-1]


"""get input data that is either a 'number' or a 'string' """
# input_font = pygame.font.sysFont("Arial", 60)
# input_rect = pygame.Rect(80, 150, 1220, 120)
# pygame.draw.rect(surface, (0, 250, 0), input_rect)
# input_screen = font.render("?", False, (0, 0, 250))
# surface.blit(input_screen, input_rect)









if __name__ == "__main__":
    main()
