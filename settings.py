""" program: Alien_Invasion game
    Name:Tizita Getachew
    Purpose: setting class of the game
    Date: 7/129/2026
"""

class Settings:
    def __init__(self):
        #Intialize the game's settings.
        self.screen_width=800
        self.screen_height = 500
        self.bg_color=(15,15,25)
        # ship settings
        self.ship_speed =1.5
        # Bullet settings
        self.bullet_speed =2.0
        self.bullet_width =6
        self.bullet_height =70
        self.bullet_color = (0,255,100)
        self.bullet_allowed = 4