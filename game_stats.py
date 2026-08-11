""" program: Alien_Invasion game
    Name:Tizita Getachew
    Purpose: GameStats class
    Date: 08/05/2026
"""
class GameStats:
  """Track statistics for Alien Invastion ."""
  def __init__(self,ai_game):
    self.settings = ai_game.settings
    self.reset_stats()
    self.prep_high_score()
  def reset_stats(self):
   self.ships_left = self.settings.ship_limit
   self.high_score = 0
  

  
