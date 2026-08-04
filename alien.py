import pygame 
import random
from pygame.sprite import Sprite
class Alien(Sprite):
   def __init__(self,ai_game):
     super().__init__()
     self.screen = ai_game.screen
     self.settings = ai_game.settings
     if not hasattr (self.settings,"alien_surface"):
        image = pygame.image.load(self.settings.alien_image)
        image = pygame.transform.rotate(image,-90)
        image =pygame.transform.scale(image,(35,35))
        self.settings.alien_surface = image

     self.image =self.settings.alien_surface
     self.rect = self.image.get_rect()
     
     self.x= float(self.rect.x)
     self.y = float(self.rect.y)