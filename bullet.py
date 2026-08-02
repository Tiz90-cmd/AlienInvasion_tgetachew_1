""" program: Alien_Invasion game 
    Name:Tizita Getachew
    Purpose: Bullet class of Alien_Inavsion game
    Date: 7/29/2026
"""

import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_game):
        # Creat a bullet object at the ship's current position.
        super().__init__()
        self.screen =ai_game.screen
        self.settings =ai_game.settings
        self.color =self.settings.bullet_color
        # creat a bullet at (0,0) and set it correct position.
        self.rect =pygame.Rect(0,0,self.settings.bullet_width,
                               self.settings.bullet_height)
        self.rect.midleft = ai_game.ship.rect.midright
        self.x =float(self.rect.x)
    def update(self):
        #Update the exact position of the bullet.
        self.x += self.settings.bullet_speed
        self.rect.x =self.x
    def draw_bullet(self):
        #Draw the bullet to the screen
        pygame.draw.rect(self.screen,self.color,self.rect)