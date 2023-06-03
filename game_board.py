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
    # picture = r"C:\Users\Sells\PycharmProjects\anthony_steve_wheel_of_fortune\player_pictures\anthony_steve.jpg"
    picture = r"C:\Users\ajh08_idy4tts\Documents\anthony_steve_wheel_of_fortune\player_pictures\anthony_steve.jpg"
    clue_surface(picture, game_surface)

    # create input screen and obtain number of players and their names
    input_message(game_surface, 'Enter the number of people playing (1, 2, or 3)?')
    pygame.display.flip()
    # time.sleep(2)
    input_okay = True
    while input_okay:
        num_of_players = get_input("string", game_surface)
        if num_of_players in ("1", "2", "3"):
            input_okay = False
    number_of_players = int(num_of_players)
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
    letters_in_alphabet = list("abcdefghijklmnopqrstuvwxyz")
    os.chdir(game_path + r'\image')
    text_list = os.listdir()

    # text_list = read_file(game_path + r"\Animals_1.txt")
    rewards_list = read_file(game_path + r"\wheel_of_fortune_rewards.txt")
    picture = choose_item(text_list)
    text_to_be_solved = picture.replace('.jpg', "").lower()
    text_to_be_solved = text_to_be_solved.replace('-', ' ')
    print('Game Board line 69 picture to be solved', picture, '  xx   ',  text_to_be_solved)
    clue_surface(picture, game_surface)
    player_loop(text_to_be_solved, active_player, continue_running_game, continue_solving_text, letters_in_alphabet,
                number_of_players, player, name_score, rewards_list, text_list, game_surface)

    # if input("Continue Playing Game y or n:  ") == "n":
    #     quit()
    # time.sleep(10)


def game_screen():
    screen = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption("Anthony's Animal Wheel of Fortune")
    screen.fill((255, 0, 0))
    pygame.display.flip()
    return screen


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
    # player_data_path = r"C:\Users\sells\PycharmProjects\anthony_steve_wheel_of_fortune\player_pictures"
    player_data_path = r"C:\Users\ajh08_idy4tts\Documents\anthony_steve_wheel_of_fortune\player_pictures"
    os.chdir(player_data_path)
    x, y = 20, 380
    blank_name_score = [["      ", "      ", "      "], ["   ", "   ", "   "], ["  ", "  ", "  "]]
    font = pygame.font.SysFont("Arial", 30)
    for row in range(3):
        for column in range(number_of_players):
            rec = pygame.Rect(x + 220 * column, y + 40 * row, 300, 40)
            pygame.draw.rect(surface, (0, 0, 255), rec, 0)
            text_surface = font.render(blank_name_score[row][column].title(), False, (0, 255, 0))
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
        # eventually the follow data will come from a file
        name_score = [["bugs", "daffy", "sam"], ["0", "0", "0"], ["0", "0", "0"]]

    else:
        player1_image = pygame.image.load(find_player_image(name_score[0][0]))
        player1_image = pygame.transform.scale(player1_image, (200, 200))
        surface.blit(player1_image, (20, 500))
        player2_image = pygame.image.load(find_player_image(name_score[0][1]))
        player2_image = pygame.transform.scale(player2_image, (200, 200))
        surface.blit(player2_image, (320, 500))
        player3_image = pygame.image.load(find_player_image(name_score[0][2]))
        player3_image = pygame.transform.scale(player3_image, (200, 200))
        surface.blit(player3_image, (620, 500))
        pygame.display.flip()

    # Set up rectangle space for player data
    number_of_players = 3
    x, y = 20, 380
    font = pygame.font.SysFont("Arial", 30)
    for row in range(3):
        for column in range(number_of_players):
            rec = pygame.Rect(x + 220 * column, y + 40 * row, 300, 40)
            pygame.draw.rect(surface, (0, 0, 0), rec, 1)
            text_surface = font.render(name_score[row][column].title(), False, (0, 255, 0))
            surface.blit(text_surface, ((x + 10) + (320 * column), (y + 10) + (row * 35)))
            pygame.display.flip()
    return surface


def find_player_image(name):
    list_of_past_players = os.listdir()
    for player in list_of_past_players:
        temp = player.replace('.jpg', '')
        if temp.lower() == name.lower():
            image_file_name = player
            return image_file_name
    image_file_name = 'sam.jpg'
    return image_file_name


def player_loop(text_to_be_solved, active_player, continue_running_game, continue_solving_text, letters_in_alphabet, number_of_players, player, name_score, rewards_list, text_list, surface):
    """ Loop through 1 to 3 players until game problem is solved
     each player gets to guess a new letter or vowel
     if the text includes the letter the player gets another turn"""
    while continue_running_game:
        # determine which player starts the game round.
        # active_player = starting_player(player_score, number_of_players)
        active_player = 0

        letters_guessed = []                          # this will be a list of all guessed letters during a single round
        letter_to_be_guessed = find_letters(text_to_be_solved)   # this is the text str changed to a list of its letters
        print(text_to_be_solved)
        spaces = text_to_be_solved.count(" ")
        number_of_letters_in_text = len(text_to_be_solved) - spaces
        partially_solved_text = []                # partially_solved_text is list of characters as the text is filled in

        continue_solving_text, partially_solved_text, solution = process_letter(" ", partially_solved_text, text_to_be_solved)
        solution_board(surface, partially_solved_text)
        guess = " "

        while continue_solving_text:
            # Show the text and a picture on a game board and get player's guess
            pygame.display.flip()
            # ---
            solution_board(surface, partially_solved_text)
            pygame.display.flip()

            # select a reward or penalty
            reward = int(choose_item(rewards_list))

            if active_player >= number_of_players:
                active_player = 0

            # input a players guess
            input_message(surface, f"{name_score[0][active_player]}, the hidden text has {number_of_letters_in_text} letters and {spaces} spaces.The guess value is {reward}")
            pygame.display.flip()
            guess = get_input("string", surface)
            # guess = input(
            # f"{name_score[0][active_player]}'s score is: {name_score[1][active_player]}.  Reward for correct letter is {reward}.  Input a letter:  ")
            score = int(name_score[1][active_player])
            if guess not in letters_in_alphabet:
                score -= reward
                name_score[1][active_player] = str(score)
                player_surface(surface, name_score, number_of_players)
                input_message(surface, "You did not type a letter!!!  Next Player.")
                time.sleep(3)
                input_message(surface,"Input not a letter.  Next Player")
                active_player += 1
                continue
            elif guess in letters_guessed:
                score -= reward
                name_score[1][active_player] = str(score)
                player_surface(surface, name_score, number_of_players)
                input_message(surface, "Don't be a doofus. This letter was already guessed! Next Player.")
                time.sleep(3)
                active_player += 1
                continue
            elif guess not in letter_to_be_guessed and guess in ["a", "e", "i", "o", "u"]:
                score -= 250
                name_score[1][active_player] = str(score)
                player_surface(surface, name_score, number_of_players)
                input_message(surface, "Sorry, but your vowel is not in the text")
                time.sleep(3)
                active_player += 1
                continue
            elif guess in ["a", "e", "i", "o", "u"]:
                score -= 250
                name_score[1][active_player] = str(score)
                player_surface(surface, name_score, number_of_players)
            elif guess in text_to_be_solved:
                score += letter_to_be_guessed.count(guess) * reward
                name_score[1][active_player] = str(score)
                player_surface(surface, name_score, number_of_players)
            elif guess not in letter_to_be_guessed:
                score -= reward
                name_score[1][active_player] = str(score)
                player_surface(surface, name_score, number_of_players)
                input_message(surface, f"Sorry, there is no {guess} in the text.")
                time.sleep(3)
                active_player += 1
                continue

            letters_guessed.append(guess)
            continue_solving_text, partially_solved_text, solution = process_letter(guess, partially_solved_text, text_to_be_solved)
            if not continue_solving_text:
                solution_board(surface, partially_solved_text)
                input_message(surface, "Game over!!   Do you want to continue playing?  y or n")
                x = get_input('string', surface)
                if x == "y":
                    print(type(text_to_be_solved))
                    print(text_to_be_solved)
                    text_to_be_solved = choose_item(text_list).lower()
                    temp_list = "C:/Users/ajh08_idy4tts/Documents/anthony_steve_wheel_of_fortune/image/"
                    text_to_be_solved = temp_list + text_to_be_solved
                    picture = choose_item(text_to_be_solved)


                    clue_image = pygame.image.load(picture)
                    clue_image = pygame.transform.scale(clue_image, (400, 400))
                    surface.blit(clue_image, (950, 300))
                    pygame.display.flip()
                    text_to_be_solved = picture.replace('.jpg', "").lower()
                    text_to_be_solved = text_to_be_solved.replace('-', ' ')
                    continue_running_game = True
                else:
                    time.sleep(10)
                    quit()
            pygame.display.flip()


def clue_surface(clue_file, surface):
    """The clue_surface shows a picture related to the text to be solved"""
    # Find on your computer the folder locations for animal pictures.
    # animal_jpgs_path = r"C:\Users\Sells\PycharmProjects\anthony_steve_wheel_of_fortune\image"
    animal_jpgs_path = r"C:\Users\ajh08_idy4tts\Documents\anthony_steve_wheel_of_fortune\image"

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


if __name__ == "__main__":
    main()
