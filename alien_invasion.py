""" program: Alien_Invasion game
    Name:Tizita Getachew
    Purpose: The main function of the game
    Date: 08/05/2026
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from time import sleep

class AlienInvasion:
    def __init__(self):
        # Intialize the game, and create game's resources
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((650,500))
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height =self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship=Ship(self)
        self.game_active =False
        self.play_button = Button(self,"play")
        self.bullets =pygame.sprite.Group()
        self.aliens =pygame.sprite.Group()
        self._create_fleet()
        self.clock=pygame.time.Clock()
        self.bg_color=(15,15,25)
    def run_game(self):
        # start the main loop of the game.
        while True:
           self._check_events()
           if self.game_active:
               self.ship.update()
               self.bullets.update()
               self._update_bullets()
               self._update_aliens()
               self._check_bullet_alien_collisions()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos= pygame.mouse.get_pos()
                 self._check_play_button(mouse_pos)

                
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
        self._check_bullet_alien_collisions()
    def _check_bullet_alien_collisions(self):
        # Remove any bullets and aliens that have collied
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
         for aliens in collisions.values():
            self.stats.score += self.settings.alien_points * len(self.aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens: 
           #Destroy exisiting bullet and create a new fleet.
             self.bullets.empty()
             self._create_fleet()
             self.settings.increase_speed()
            # Increase level.
             self.stats.level += 1
             self.sb.prep_level()

    def _update_aliens(self):
         self.aliens.update()
         for alien in self.aliens.copy():
             if alien.rect.right <0:
                self.aliens.remove(alien)
         if not self.aliens and self.game_active:
                  self._create_fleet()
         # Check the collision between ship and alien
         if pygame.sprite.spritecollideany(self.ship,self.aliens):
             self._ship_hit()
             

    def _update_screen(self):
        #Update image on the screen, and flip to new screen.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Draw the score information.
        self.sb.show_score()
        #Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
    def _create_fleet(self):
        """ create a full fleet and calculating space based on the size 
        of the alien and screen dimensions.
        """
        alien = Alien(self)
        alien_width,alien_height =alien.rect.size

        current_x = self.settings.screen_width - alien_width* 2
        current_y = alien_height 

        x_spacing =alien_width *2.5
        y_spacing =alien_height* 2
        # create alien based on avilable screen dimension and alien size.
        while current_y < (self.settings.screen_height - alien_height * 2):
            while current_x  >  self.settings.screen_width * 0.35:
                         
                self._create_alien (current_x,current_y)
                current_x -= x_spacing     
            current_x = self.settings.screen_width - alien_width*2
            current_y += y_spacing    


    def _create_alien(self,current_x,current_y):
    # Create aline in the position of (x,y).
        new_alien =Alien(self)
        new_alien.rect.x=current_x
        new_alien.rect.y =current_y
        new_alien.x =float(current_x)
        new_alien.x =float(new_alien.rect.x)
        new_alien.y =float(new_alien.rect.y)
        self.aliens.add(new_alien)
    
    def _ship_hit(self):
      # ship respond when hit by ann aliens.
      if self.stats.ships_left > 0:
        # Decrement ships_left , and update scoreboard.
        self.stats.ships_left -= 1
        self.sb.prep_ships()
        #Get rid of any remaing bullet and aliens
        self.bullets.empty()
        self.aliens.empty()
        # create a new fleet and pause.
        self._create_fleet()
        self.ship.center_ship()
        sleep(0.5)
      else:
         self.game_active =False
         pygame.mouse.set_visible(True)
    def _check_play_button(self,mouse_pos):
        """Start a new game when the player clicks plays"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            #Reset the game statistics
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active =True
        # Get rid of any remaining bullets and aliens:
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    
