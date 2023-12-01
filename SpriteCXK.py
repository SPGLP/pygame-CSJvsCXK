""" 偶像练习生：蔡徐坤 """
""" 喜欢的话，就多多为我投票吧 """

from typing import Any
import pygame
from pygame.sprite import *
import random

class SpriteCXK(pygame.sprite.Sprite):
    """ 偶像练习生：蔡徐坤 """

    arrowLeft = True

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(".\CXK.jpg")
        self.rect = self.image.get_rect()
        self.rect.y = 350
        self.randomSpeed()                              # 初始化移动速度
    
    def update(self):
        if self.arrowLeft == True:
            self.rect.x += self.speed
            if self.rect.x >= 550:
                self.arrowLeft = False
        else :
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.arrowLeft = True

    def randomSpeed(self):
        self.speed = random.randint(1, 10)              # 移动速度