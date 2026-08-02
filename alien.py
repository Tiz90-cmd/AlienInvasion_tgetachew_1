import pygame 
import random
from pygame.sprite import Sprite
class Alien(Sprite):
   def __init__(self,ai_game):
     super().__init__()
     self.screen = ai_game.screen
     self.settings = ai_game.settings
     self.image = pygame.image.load(self.settings.alien_image)
     self.rect = self.image.get_rect()
     self.rect.x =self.settings.screen_width - self.rect.width
     self.rect.y = random.randint(50,self.settings.screen_height - 50)
     self.x= float(self.rect.x)
     self.y = float(self.rect.y)