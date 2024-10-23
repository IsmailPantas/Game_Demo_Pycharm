import pygame
import button
import b
import level_archer


def map():
    pygame.init()
    genislik = 800
    yukseklik = 550
    pencere = pygame.display.set_mode((genislik, yukseklik))
    # görseller
    map = pygame.image.load("map.png")
    map = pygame.transform.scale(map, (map.get_height() / 1.2, map.get_width() * 0.36))
    music_button = pygame.image.load("music_button.png")
    lvl_bandits = pygame.image.load("lvl_bandits.png")
    lvl_archer = pygame.image.load("lvl_archer.png")

    # butonlar
    music_button = button.Button(pencere, 750, 20, music_button, 30, 30)
    lvl_bandits_button = button.Button(pencere, 600, 170, lvl_bandits, 50, 50)
    lvl_archer_button = button.Button(pencere, 630, 350, lvl_archer, 50, 50)
    durum = True
    while durum:
        pencere.blit(map, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                durum = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl_bandits_button.is_clicked(event):
                    # durum = False
                    b.baslat()
                if lvl_archer_button.is_clicked(event):
                    level_archer.baslat()
        music_button.draw()
        lvl_bandits_button.draw()
        lvl_archer_button.draw()
        pygame.display.update()


pygame.quit()
