import pygame

from models import Asteroid, GameObject, Spaceship
from utils import get_random_position, load_sprite


class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self) -> None:
        self.init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)

        # game speed based on pygame clock
        self.clock = pygame.time.Clock()

        # self.asteroids = [Asteroid(get_random_position(self.screen)) for _ in range(6)]
        self.asteroids = []
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append)

        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break

            self.asteroids.append(Asteroid(position))

    def game_loop(self):
        while True:
            self.handle_input()
            self.process_game_logic()
            self.draw()

    def get_game_objects(self):
        game_ojbects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            game_ojbects.append(self.spaceship)

        return game_ojbects

    def init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks Rocks")

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                quit()

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            elif is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    def process_game_logic(self):
        # loop through all game objects and move them
        for game_object in self.get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    break

    def draw(self):
        # self.screen.fill((0, 0, 250))
        # draw order: earlier lines of code are "lower"
        self.screen.blit(self.background, (0, 0))

        # loop through all game objects and draw them
        for game_object in self.get_game_objects():
            game_object.draw(self.screen)

        pygame.display.flip()
        # 60 fps
        self.clock.tick(60)
