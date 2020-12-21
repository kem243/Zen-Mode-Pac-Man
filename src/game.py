"""Module containing the Game class"""
import pygame

from spritesheet import Spritesheet
from tiledmap import TiledMap
from constants import TILESIZE, DISPLAY_H, DISPLAY_W

class Game:
    def __init__(self):
        pygame.init()
        self.canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
        self.window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
        self.running = True

        self.sprites = pygame.sprite.Group()
        self.load_data()
        

    def load_data(self):
        """Loads pertinent data for the game"""
        # Map initialization
        map = TiledMap(r'../assets/stage_1.tmx')
        self.map_image = map.make_map()
        map_rect = self.map_image.get_rect()

        # Sprite initialization
        my_spritesheet = Spritesheet(r'../assets/sprites.png')
        self.open_mouth = my_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE)
        self.player = Player(self, self.open_mouth)

    def update(self):
        """"""
        self.sprites.update()

    def draw(self):
        """"""
        self.canvas.fill((0,0,0))
        self.canvas.blit(self.map_image, (0, 0))
        for sprite in self.sprites:
            self.canvas.blit(sprite.image, sprite.pos)
        # self.canvas.blit(self.open_mouth, (TILESIZE, TILESIZE))
        self.window.blit(self.canvas, (0,0))

    def run(self):
        """Game loop"""
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()

            self.draw()
            pygame.display.update()

class Player(pygame.sprite.Sprite):
    """Class to represent pacman"""
    def __init__(self, game: Game, image: pygame.Surface):
        super().__init__(game.sprites)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(1, 1) * TILESIZE
        self.rect.center = self.pos

    def update(self):
        """"""
        self.pos.x = (self.pos.x + 1) % DISPLAY_W
        self.rect.center = self.pos     
