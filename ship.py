import pygame
class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.image = pygame.image.load('image/ship.bmp')
        self.image =pygame.transform.rotate(self.image,-90)
        self.rect=self.image.get_rect()
        self.rect.left=self.screen_rect.left
        self.rect.centery=self.screen_rect.centery
    def blitme(self):
        self.screen.blit(self.image,self.rect)