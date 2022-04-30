"""This program uses pygame to display three pictures"""
import time
import pygame
import random
import os
import sys


def main():
    # time.sleep(10)
    pygame.init()
    surface = pygame.display.set_mode((1400, 700))
    pygame.display.set_caption("Anthony's Pictures")
    surface.fill((255, 0, 0))
    pygame.display.flip()
    # Find image directory
    path = os.getcwd()
    print(path)
    picture_path = path + r"\image"
    print(picture_path)

    # time.sleep(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        show_picture(picture_path, surface)


def pick_picture(path):
    os.chdir(path)
    pick_your_file_titles = os.listdir()
    picture = random.choice(pick_your_file_titles)
    return picture


def show_picture(path, surface):
    # Get 3 pictures
    display = []
    for a in range(3):
        b = pick_picture(path)
        display.append(b)

    # Display pictures
    for c in range(3):
        d = display[c]
        p_image = pygame.image.load(d)
        p_image = pygame.transform.scale(p_image, (400, 400))
        surface.blit(p_image, (((20 + 400) * c) + 20, 100))
    pygame.display.flip()
    # Display titles
    for index in range(3):
        pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(((60 + 400) * index) + 10, 480, 360, 80))
    font = pygame.font.SysFont("Ariel", 30)
    for index in range(3):
        text_surface = font.render(display[index], False, (0, 255, 0))
        surface.blit(text_surface, (((60 + 400) * index) + 40, 500))
    pygame.display.flip()
    time.sleep(5)


if __name__ == "__main__":
    main()
