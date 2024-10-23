import pygame
# import map
from pyvidplayer import Video
import main_menu

pygame.init()

pencere = pygame.display.set_mode((800, 550))
vid = Video("game_intro.mp4")
vid.set_size((800, 550))

font = pygame.font.SysFont('arial', 20)


def yazi_yaz(yazi, font, yazi_rengi, x, y, arka_rengi):
    img = font.render(yazi, True, yazi_rengi, arka_rengi)
    pencere.blit(img, (x, y))


durum = True
while durum:

    vid.draw(pencere, (0, 0))
    yazi_yaz('Geçmek için "Mouse" tuşuna basınız', font, (0, 0, 0), 25, 25, (255, 255, 255))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            durum = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            vid.close()
            main_menu.baslat()
            # map.map()
    if vid.end:
        vid.close()
        main_menu.baslat()
    # map.map()

pygame.quit()
