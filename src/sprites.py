"""Module containing the sprites"""

import pygame

from constants import PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    """Class to represent pacman"""
    def __init__(self, game, image: pygame.Surface, x: int, y: int) -> None:
        super().__init__(game.all_sprites)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x + self.rect.width / 2
        self.y = y + self.rect.width / 2
        self.rect.center = (self.x, self.y)
        self.velocity = pygame.math.Vector2(PLAYER_SPEED, 0)

    def get_keys(self) -> None:
        """Sets velocity based on the pressed key"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity.x = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity.x = PLAYER_SPEED
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity.y = -PLAYER_SPEED
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity.y = PLAYER_SPEED

    def collide_with_walls(self, group: pygame.sprite.AbstractGroup, dir: str) -> None:
        """Checks whether this sprite has collided with any sprite in the given group
        in the given direction
        """
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, group, False)
            if hits:
                if hits[0].rect.centerx > self.rect.centerx:
                    self.x = hits[0].rect.left - self.rect.width / 2
                if hits[0].rect.centerx < self.rect.centerx:
                    self.x = hits[0].rect.right + self.rect.width / 2
                self.velocity.x = 0
                self.rect.centerx = self.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, group, False)
            if hits:
                if hits[0].rect.centery > self.rect.centery:
                    self.y = hits[0].rect.top - self.rect.height / 2
                if hits[0].rect.centery < self.rect.centery:
                    self.y = hits[0].rect.bottom + self.rect.height / 2
                self.velocity.y = 0
                self.rect.centery = self.y
    
    def update(self) -> None:
        """Updates the sprite's position"""
        self.get_keys()
        self.x += self.velocity.x * self.game.dt
        self.y += self.velocity.y * self.game.dt
        self.rect.centerx = self.x
        self.collide_with_walls(self.game.walls, 'x')
        self.rect.centery = self.y
        self.collide_with_walls(self.game.walls, 'y')

class Wall(pygame.sprite.Sprite):
    """A sprite to represent a wall/obstacle in the game"""
    def __init__(self, game, x, y, width, height):
        super().__init__(game.walls)
        self.game = game
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y