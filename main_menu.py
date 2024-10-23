import pygame
import map
import button


def baslat():
    pygame.init()
    genislik = 800
    yukseklik = 550
    pencere = pygame.display.set_mode((genislik, yukseklik))
    background = pygame.image.load("mountain_bg.png")
    background = pygame.transform.scale(background, (background.get_width() * 2.1, background.get_height() * 2.6))
    play_button = pygame.image.load("play_button.png")
    info_button = pygame.image.load("info_button.png")
    option_button = pygame.image.load("options_button.png")
    quit_button = pygame.image.load("quit_button.png")
    game_logo = pygame.image.load("game_logo.png")
    game_logo = pygame.transform.scale(game_logo, (game_logo.get_width() / 1.8, game_logo.get_height() / 1.8))

    def yazi_yaz(yazi, font, yazi_rengi, x, y, arka_rengi=(0, 0, 0)):
        img = font.render(yazi, True, yazi_rengi, arka_rengi)
        return img

    def bghill_ciz():
        pencere.blit(background, (0, 0))

    font = pygame.font.SysFont('arial', 32)

    play_button = button.Button(pencere, 310, 210, play_button, 200, 70)
    option_button = button.Button(pencere, 310, 290, option_button, 200, 70)
    quit_button = button.Button(pencere, 310, 370, quit_button, 200, 70)
    info_button = button.Button(pencere, 740, 10, info_button, 50, 50)

    durum = True
    while durum:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                durum = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.is_clicked(event):
                    map.map()
                    #durum = False
                if quit_button.is_clicked(event):
                    durum = False

        bghill_ciz()
        pencere.blit(game_logo, (180, -70))
        play_button.draw()
        option_button.draw()
        quit_button.draw()
        info_button.draw()
        pygame.display.update()


pygame.quit()
