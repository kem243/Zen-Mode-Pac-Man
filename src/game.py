"""Module containing the Game class"""
import pygame

from spritesheet import Spritesheet
from tiledmap import TiledMap
from constants import TILESIZE, DISPLAY_H, DISPLAY_W
from sprites import Player, Wall

class Game:
    """Top-level class to represent a single game of pacman"""
    def __init__(self):
        pygame.init()
        self.canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
        self.window = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(10, 10)
        self.running = True

        self.load_data()
        self.new()
        self.dt = 0

    def load_data(self):
        """Loads pertinent data for the game"""
        # Map initialization
        self.map = TiledMap(r'../assets/stage_1.tmx')
        self.map_image = self.map.make_map()
        map_rect = self.map_image.get_rect()

        # Sprite initialization
        my_spritesheet = Spritesheet(r'../assets/sprites.png')
        self.open_mouth = my_spritesheet.get_sprite(0, 0, TILESIZE, TILESIZE)

    def new(self):
        """Initializes data and sprites"""
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        for tile_object in self.map.tmxdata.objects:
            if tile_object.type == 'wall':
                Wall(self, tile_object.x, tile_object.y,
                     tile_object.width, tile_object.height)
            if tile_object.type == 'player':
                self.player = Player(self, self.open_mouth,
                                     tile_object.x, tile_object.y)

    def handle_events(self):
        """Handles events done by the player"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Updates all sprites"""
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, DISPLAY_W, TILESIZE):
            pygame.draw.line(self.canvas, (255, 0, 0), (x, 0), (x, DISPLAY_H))
        for y in range(0, DISPLAY_H, TILESIZE):
            pygame.draw.line(self.canvas, (255, 0, 0), (0, y), (DISPLAY_W, y))

    def draw(self):
        """Draws map and sprite onto the screen"""
        self.canvas.fill((0,0,0))
        self.canvas.blit(self.map_image, (0, 0))
        # self.draw_grid()
        for sprite in self.all_sprites:
            self.canvas.blit(sprite.image, self.player.rect)
        self.window.blit(self.canvas, (0,0))

    def run(self):
        """Game loop"""
        while self.running:
            self.dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
