import pygame
class ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen=ai_game.screen.get_rect()
        self.image = pygame.image.load('image/octagon_ship.bmp')
        self.rect=self.image.get_rect()
        self.rect.left=self.screen_rect.left
        self.rect.centery=self.screen_rect.centery
    def blitme(self):
        self.screen.lit(self.image,self.rect)