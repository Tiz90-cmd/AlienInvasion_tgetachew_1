import pygame 
import random
from pygame.sprite import Sprite
class Alien(Sprite):
   def __init__(self,ai_game):
     super().__init__()
     self.screen = ai_game.screen
     self.settings = ai_game.settings
     
     self.image = pygame.image.load(self.settings.alien_image)
     self.image = pygame.transform.rotate(self.image,-90)
     self.image = pygame.transform.scale(self.image,(30,30))
     self.rect = self.image.get_rect()
     
   def update(self):
      self.x += self.settings.alien_speed * self.settings.fleet_direction
      self.rect.x =self.x
      self.rect.y = self.y
   def check_edges(self):
      screen_rect =self.screen.get_rect()
      return self.rect.left <=0 or self.rect.right >= screen_rect.right