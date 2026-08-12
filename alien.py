""" program: Alien_Invasion game
    Name:Tizita Getachew
    Purpose: Alien class of the game
    Date: 8/12/2026
"""

import pygame 
import random
from pygame.sprite import Sprite
class Alien(Sprite):
   def __init__(self,ai_game):
     super().__init__()
     self.screen = ai_game.screen
     self.settings = ai_game.settings
     #Load alien image
     self.image = pygame.image.load(self.settings.alien_image)
     self.image = pygame.transform.rotate(self.image,-90)
     self.image = pygame.transform.scale(self.image,(30,30))
     #Position align on right side
     self.rect = self.image.get_rect()
     self.rect.right =self.screen.get_rect().right-10
     self.rect.y = self.settings.screen_height//2
     # store x and y position
     self.x = float(self.rect.x)
     self.y = float(self.rect.y)
     
   def update(self):
     # Move left toward the ship
     self.x -= self.settings.alien_speed

     self.rect.x =self.x
     self.rect.y =self.y

   def check_edges(self):
      screen_rect =self.screen.get_rect()
      return self.rect.left <=0
      

      