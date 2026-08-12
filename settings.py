""" program: Alien_Invasion game
    Name:Tizita Getachew
    Purpose: setting class of the game
    Date: 8/05/2026
"""
from pathlib import Path
class Settings:
    def __init__(self):
        #Intialize the game's settings.
        self.screen_width=800
        self.screen_height = 500
        self.bg_color=(15,15,25)
        # ship settings
        self.base_bath = Path(__file__).parent
        self.ship_image = self.base_bath/'image'/'ship.bmp'
        self.ship_speed =2
        #self.alien_image = self.base_bath/'image'/'alien.bmp'
        self.ship_limit = 4
        # Bullet settings
        self.bullet_speed =1
        self.bullet_width = 8
        self.bullet_height = 99
        self.bullet_color = (0,255,0)
        self.bullet_allowed = 4
        #Alien settings
        self.alien_image = self.base_bath/'image'/'alien.bmp'
        self.alien_speed =1.5
        #How quickly the game speed up
        self.speedup_scale =1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        #Initialize settins that chanhe throughout the game.
        self.ship_speed =10
        self.bullet_speed =5
        self.alien_speed = 1.5
        self.fleet_direction = 1
        #scoring settings.
        self.alien_points = 50
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)

       