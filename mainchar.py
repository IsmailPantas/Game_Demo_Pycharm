import pygame
import random
from screen import Pencere
pygame.init()


pencere = Pencere()

class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        # self.start_shield = shield
        # self.shield = shield
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0: idle 1: attack 2: hurt 3: dead
        self.update_time = pygame.time.get_ticks()

        # load idle images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"img/{self.name}/Idle/{i}.png")
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # load attack images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"img/{self.name}/Attack/{i}.png")
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # load hurt images
        temp_list = []
        for i in range(3):
            img = pygame.image.load(f"img/{self.name}/Hurt/{i}.png")
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        # load death images
        for i in range(10):
            img = pygame.image.load(f"img/{self.name}/Death/{i}.png")
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
            self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100
        # handle images
        # update images
        self.image = self.animation_list[self.action][self.frame_index]
        # check time point
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # reset animation
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, target):
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        target.hurt()
        # check target death
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
            #   damage_text = DamageText(target.rect.centerx,target.rect.y,str(damage),red)
            #   damage_text_group.add(damage_text)
            #   run attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def hurt(self):
        # set hurt animaton
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def death(self):
        # set death animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def reset(self):
        self.alive = True
        self.potions = self.start_potions
        self.hp = self.max_hp
        # self.shield = self.start_shield
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self, hp):
        # buraya pencere sınıfı çağırılacak
        pencere.screen.blit(self.image, self.rect)

# class HealthBar():
#     def __init__(self,x,y,hp,max_hp):
#         self.x = x
#         self.y = y
#         self.hp = hp
#         self.max_hp = max_hp
#
#     def draw(self,hp):
#         # update to new health
#         self.hp = hp
#         # calculate rati o
#         rati o = self.hp /self.max_hp
#         pygame.draw.rect(baslat().screen, (255,0,0),(self.x,self.y,150,20))
#         pygame.draw.rect(baslat().screen, (0,255,0),(self.x,self.y,150*20))
