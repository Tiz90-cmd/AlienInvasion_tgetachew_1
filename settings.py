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
        self.ship_speed =1.5
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
       