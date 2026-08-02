""" program: Alien_Invasion game
    Name:Tizita Getachew
    Purpose: The main function of the game
    Date: 7/29/2026
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class AlienInvasion:
    def __init__(self):
        # Intialize the game, and create game's resources
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((650,500))
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height =self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        self.bullets =pygame.sprite.Group()
        self.aliens =pygame.sprite.Group()
        self._create_fleet()
        self.clock=pygame.time.Clock()
        self.bg_color=(15,15,25)
    def run_game(self):
        # start the main loop of the game.
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    def _check_events(self):
        #keypresess and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                 self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        # keypresses. 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right =True
        elif event.key ==pygame.K_LEFT:
            self.ship.moving_left =True
        elif event.key == pygame.K_UP:
             self.ship.moving_up =True
        elif event.key ==pygame.K_DOWN:
             self.ship.moving_down = True
        #  Space keypress for firing.
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()
        # Quiting the game
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
    def _check_keyup_events(self,event):
       # key releases.
       if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
       elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
       elif event.key == pygame.K_UP:
             self.ship.moving_up = False
       elif event.key == pygame.K_DOWN:
             self.ship.moving_down =False
    def _fire_bullet(self):
        # create a bullet and add it to the bullet group.
        if len(self.bullets)< self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        # Update bullet positions.
        self.bullets.update()
        #Get rid off of bullets that have fired.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
           
    def _update_screen(self):
        #Update image on the screen, and flip to new screen.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    
