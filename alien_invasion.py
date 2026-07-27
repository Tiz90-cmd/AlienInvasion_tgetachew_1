import sys
import pygame
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.clock=pygame.time.clock()
        self.bg_color=(230,230,230)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)






if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    
