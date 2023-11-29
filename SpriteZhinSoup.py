""" 鸡汤来咯 """
""" 不咸不淡，味道真是好极了 """

from typing import Any
import pygame
from pygame.sprite import *

class SpriteZhinSoup(pygame.sprite.Sprite):
        
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load(r".\zhinsoup.jpg")
        self.rect = self.image.get_rect()
        # self.rect.y = 0
        self.rect.x = x
        # self.speed = random.randint(1, 10)
        self.speed = 10                                  # 移动速度

    def update(self):
        self.rect.y += self.speed

