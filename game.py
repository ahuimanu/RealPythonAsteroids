import pygame

class SpaceRocks:
    def __init__(self) -> None:
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
    
    def game_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.draw()

    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks Rocks")

    def handle_input(self):
        pass

    def process_game_logic(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 250))
        pygame.display.flip()

