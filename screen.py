import pygame

pygame.init()


class Pencere():
    bottom_panel = 150
    screen_width = 800
    screen_height = 400 + bottom_panel
    screen = pygame.display.set_mode((screen_width, screen_height))

