""" 高级特工：穿山甲 """
""" 啊哈哈哈哈！我滴任务完成力！ """

from typing import Any
import pygame
from pygame.sprite import *

class SpriteCSJ(pygame.sprite.Sprite):
    """ 高级特工：穿山甲 """

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(".\CSJ.jpg")
        self.rect = self.image.get_rect()
        #self.rect.y = 0
        #self.speed = 0                      # 移动速度
    
    def update(self):
            if self.rect.x < 0:
                 self.rect.x = 0
            if self.rect.x > 550:
                 self.rect.x = 550