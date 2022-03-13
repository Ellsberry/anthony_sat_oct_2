""" This game is for up to 3 players.  You will need the locations on your computer
 for the animal pictures and player data """
import sys
import pygame
import os
import time


def main():
    pygame.init()

    # create the over all game surface
    game_surface = game_screen()

    # create the solution text board
    solution_board(game_surface, "Wheel of Fortune")
    pygame.display.flip()

    # create the initial player surface with 3 players
    player_surface(game_surface)

    # show game masters of ceremony
    # picture = r"C:\Users\Steve Ellsberry\PycharmProjects\anthony_steve_wheel_of_fortune\player_pictures\anthony_steve.jpg"
    picture = r"C:\Users\ajh08_idy4tts\Documents\anthony_steve_wheel_of_fortune\player_pictures\anthony_steve.jpg"
    clue_surface(picture, game_surface)

    # create input screen and obtain number of players and their names
    input_message(game_surface, 'Enter the number of people playing (1, 2, or 3)?')
    pygame.display.flip()
    num_players = get_input("number", game_surface)
    print(num_players)
    input_message(game_surface, 'Enter name of player number 1')
    pygame.display.flip()
    player_1_name = get_input("string", game_surface)
    print("player number 1:  ", player_1_name)

    time.sleep(20)


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


def player_surface(surface, num_players = 0):
    """ This function displays player information"""
    # Find on your computer the folder location for player pictures.
    # This URL is for Steve's Computer
    # player_data_path = r"C:\Users\Steve Ellsberry\PycharmProjects\anthony_steve_wheel_of_fortune\player_pictures"
    # This URL is for Anthony's computer
    player_data_path = r"C:\Users\ajh08_idy4tts\Documents\anthony_steve_wheel_of_fortune\player_pictures"

    os.chdir(player_data_path)

    # display the following pictures if there is no picture for players
    if num_players == 0:
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
    print("Bugs' current score: ", name_score[2][1])
    # Set up rectangle space for player data
    num_players = 3
    x, y = 20, 380
    font = pygame.font.SysFont("Arial", 30)
    for row in range(3):
        for column in range(num_players):
            rec = pygame.Rect(x + 220 * column, y + 40 * row, 300, 40)
            pygame.draw.rect(surface, (0, 0, 0), rec, 1)
            text_surface = font.render(name_score[row][column], False, (0, 255, 0))
            surface.blit(text_surface, ((x + 10) + (320 * column), (y + 10) + (row * 35)))
            pygame.display.flip()
    return surface


def clue_surface(clue_file, surface):
    """The clue_surface shows a picture related to the text to be solved"""
    # Find on your computer the folder locations for animal pictures.
    # This URL is for Steve's Computer
    # animal_jpgs_path = r"C:\Users\Steve Ellsberry\PycharmProjects\anthony_steve_wheel_of_fortune\image"
    # This URL is for Anthony's computer
    animal_jpgs_path = r"C:\Users\ajh08_idy4tts\Documents\anthony_steve_wheel_of_fortune\image"

    os.chdir(animal_jpgs_path)
    clue_image = pygame.image.load(clue_file)
    clue_image = pygame.transform.scale(clue_image, (400, 400))
    surface.blit(clue_image, (950, 300))
    pygame.display.flip()


def input_message(surface, text):
    """this module shows the input requests"""
    message = text + "  and press space bar"
    font = pygame.font.SysFont("Arial", 60)
    input_rect = pygame.Rect(20, 150, 1220, 120)
    pygame.draw.rect(surface, (0, 250, 0), input_rect)
    input_screen = font.render(text, False, (0, 0, 250))
    surface.blit(input_screen, input_rect)


def get_input(type_input, surface):
    """get input data that is either a 'number' or a 'string' """
    font = pygame.font.SysFont("Arial", 60)
    input_rect = pygame.Rect(80, 150, 1220, 120)
    pygame.draw.rect(surface, (0, 250, 0), input_rect)
    input_screen = font.render("?", False, (0, 0, 250))
    surface.blit(input_screen, input_rect)
    user_text = ""
    get_user_input = True
    while get_user_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                time.sleep(2)
                pygame.quit()
                sys.exit()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        get_user_input = False
                    user_text += event.unicode
                    if type_input == "number":
                        if user_text in ['1', '2', '3']:
                            return int(user_text)
                        else:
                            break
                    else:
                        print("line 148 user text ", user_text)
        return user_text[:-1]









if __name__ == "__main__":
    main()
