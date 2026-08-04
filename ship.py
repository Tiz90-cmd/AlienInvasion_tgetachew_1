""" program: Alien_Invasion game
    Name:Tizita Getachew
    Purpose: Ship class of the game
    Date: 7/29/2026
"""
import pygame
class Ship:
    def __init__(self,ai_game):
        # Intialize the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        self.settings =ai_game.settings
        # load the image of the ship
        self.image = pygame.image.load(self.settings.ship_image)
        self.image =pygame.transform.rotate(self.image,-90)
        #position ship in left side
        self.rect=self.image.get_rect()
        self.rect.left=self.screen_rect.left
        self.rect.centery=self.screen_rect.centery
        # Store a flot the x  movement forward
        self.x =float(self.rect.x)
        #Movement flags; start with the ship that's not moving.
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
    def update(self):
        #Automatic movemnt forward util center
       # center_limit = self.screen_rect.centerx
        ##if self.rect.x < 
            #self.x += 0.5
       # Manual movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left> 0:
            self.x -= self.settings.ship_speed
       # Moving the ship up and dowm ward
        if self.moving_up and self.rect.top > 0 :
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
           self.rect.y += self.settings.ship_speed
        # Update rect object from self.x.    
        self.rect.x =self.x


    def blitme(self):
        self.screen.blit(self.image,self.rect)