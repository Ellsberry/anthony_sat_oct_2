""" This game is for up to 3 players.  You will need the locations on your computer
 for the animal pictures and player data """

import pygame
import os
import time


def main():
    initialize_game()
    # players()
    # play(game)


def initialize_game():
    """ Initialize game """

    # Find on your computer the folder locations that will be used.
    # animal_jpgs_path = r"C:\Users\sells\PycharmProjects\anthony_sat_oct_2\image"
    # player_data_path = r"C:\Users\sells\PycharmProjects\anthony_sat_oct_2\player_pictures"
    # The next 2 URLs are for Anthony's computer
    animal_jpgs_path = r"C:\imagee"
    player_data_path = r"C:\Users\ajh08\PycharmProjects\anthony_sat_oct_two\player_pictures"

    # Set up game screen
    pygame.init()
    surface = game_surface()
    player_surface = player_screen(3, player_data_path, surface)
    # text_surface()
    clue_surface(animal_jpgs_path, r"Cairn-Terrier.jpg", surface)
    # rewards_surface()
    # input_surface()
    # game_over_surface()


def game_surface():
    surface = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption("Anthony's Animal Wheel of Fortune")
    surface.fill((255, 0, 0))
    pygame.display.flip()           # this updates the entire screen
    return surface


def player_screen(num_players, player_data_path, surface):
    """ This function displays player information"""
    os.chdir(player_data_path)
    # Contains pictures of players and a player_file with previous scores and picture name

    # display pictures of the players
    player1_image = pygame.image.load('anthony.jpg')
    player1_image = pygame.transform.scale(player1_image, (200, 200))
    surface.blit(player1_image, (0, 500))
    player2_image = pygame.image.load('lisa.jpg')
    player2_image = pygame.transform.scale(player2_image, (200, 200))
    surface.blit(player2_image, (200, 500))
    player3_image = pygame.image.load('michael.jpg')
    player3_image = pygame.transform.scale(player3_image, (200, 200))
    surface.blit(player3_image, (400, 500))
    pygame.display.flip()

    # display current score.  At the beginning of game scores are 0.
    #      EVENTUALLY THE FOLLOW DATA WILL COME FROM A FILE
    name_score = [["Anthony", "Lisa", "Michael"], ["0", "0", "0"], ["5000", "2000", "1000"]]

    # Set up rectangle space for player data
    x, y = 50, 700
    blocksize = 100
    font = pygame.font.SysFont("Arial", 30)
    for row in range(2):
        for column in range(3):
            rec = pygame.Rect(x + 450 * column, y + 50 * row, 400, 50)
            pygame.draw.rect(surface, (0, 0, 0), rec, 1)
            text_surface = font.render(name_score[row][column], False, (0, 255, 0))
            surface.blit(text_surface, ((x + 10) + (450 * column), (y + 10) + (row * 50)) )
            pygame.display.flip()
    return surface


def clue_surface(animal_jpgs_path, clue_file, surface):
    os.chdir(animal_jpgs_path)
    clue_image = pygame.image.load(clue_file)
    clue_image = pygame.transform.scale(clue_image, (400, 400))
    surface.blit(clue_image, (950, 300))
    pygame.display.flip()
    time.sleep(10)


if __name__ == "__main__":
    main()