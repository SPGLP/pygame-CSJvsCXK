""" Python 真是一个神奇的语言 """
""" 面向对象的逻辑使我的眼球和大脑旋转 """

""" 穿山甲大战蔡徐坤 """

""" 
Create by SPGLP55(LSL01)
Create Date : 2023.11.25
Project CodeName : CAKEMOVE
Version : INDEV 0.0.06.231201_1 bulid 43
Description :
*****
起因是学校开发中心要弄一个 Python 小游戏作为入门测试
虽然我没报名加入这个组织，但看到舍友们都忙着用 JAVAWEB 搞网页连数据库（py游戏或java网页设计二选一），舍近求远？
于是我弄了这个出来，纯粹自己研究罢了，看看有没有那么难。
如果能帮助到舍友或者其它有需要的小伙伴也是不错的(●'◡'●)
初学Python和Pygame，三四天时间菜鸟教程看了看基本语法直接上手了，如有不足欢迎大佬 issus 或 pull Request。
*****
"""

import pygame
from SpriteCXK import *
from SpriteCSJ import *
from SpriteZhinSoup import *

class CSJVSCXKGame(object):
    """ 穿山甲大战蔡徐坤 """
    bgImage = pygame.image.load(".\gameBG.jpg")
    #SCREEN_RECT = pygame.Rect(0,0,500,400)

    def __init__(self):
        #self.screen = pygame.display.set_mode((600,400))
        #self.screen = pygame.display.set_caption("穿山甲大战蔡徐坤 Python Edition")
        self.screenDisplay = pygame.display
        self.window = self.screenDisplay.set_mode((600,400))
        self.screenDisplay.set_caption("穿山甲大战蔡徐坤 Python Edition")
        self.rect = self.bgImage.get_rect()
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        self.clickSound = pygame.mixer.Sound(".\click.ogg")    # “鸡汤来咯”
        self.hitSound = pygame.mixer.Sound(".\hit.ogg")        # “你干嘛~嗨嗨~哟~”
        self.cxk = SpriteCXK()                  # Class CXK
        self.cxkGroup = pygame.sprite.Group(self.cxk)
        self.csj = SpriteCSJ()                  # Class CSJ
        self.csjGroup = pygame.sprite.Group(self.csj)
        self.zhinSoupIsDown = False             # 是否正在投放鸡汤
        self.hitCXK = False                     # 是否击中 CXK
        self.scores = 0                         # 游戏分数

    def startGame(self):
        while True:
            self.clock.tick(30)                 # 游戏帧率
            self.window.blit(self.bgImage,(0,0))
            self.__updateSprites()
            self.__eventHandle()
            pygame.display.update()

    def __updateSprites(self):
        self.cxkGroup.update()
        self.cxkGroup.draw(self.window)
        self.csjGroup.update()
        self.csjGroup.draw(self.window)
        if self.zhinSoupIsDown:
            self.zhinSoupGroup.update()
            self.zhinSoupGroup.draw(self.window)
            self.hitCXK = pygame.sprite.collide_rect(self.zhinSoup, self.cxk)
            if self.zhinSoup.rect.y > self.window.get_height():
                self.zhinSoupIsDown = False
                pygame.sprite.Sprite.kill(self.zhinSoup)
            if  self.hitCXK:
                self.zhinSoupIsDown = False
                pygame.sprite.Sprite.kill(self.zhinSoup)
                self.hitSound.play()
                self.scores += 1
                self.WinScoreCaption = "穿山甲大战蔡徐坤 Python Edition - 当前游戏得分：" + str(self.scores)
                pygame.display.set_caption(self.WinScoreCaption)

    def __eventHandle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CSJVSCXKGame.__gameOver()

        pressedKey = pygame.key.get_pressed()
        if pressedKey[pygame.K_RIGHT] or pressedKey[pygame.K_d]:
            self.csj.rect.x += 5                 # 穿山甲右移
        elif pressedKey[pygame.K_LEFT] or pressedKey[pygame.K_a]:
            self.csj.rect.x -= 5                 # 穿山甲左移
        elif pressedKey[pygame.K_DOWN] or pressedKey[pygame.K_s] or pressedKey[pygame.K_SPACE]:
            if not self.zhinSoupIsDown:          # 投放鸡汤
                self.zhinSoupIsDown = True       
                self.zhinSoup = SpriteZhinSoup(self.csj.rect.x)
                self.zhinSoupGroup = pygame.sprite.Group(self.zhinSoup)
                self.clickSound.play()
            else:
                pass
        else:
            pass
        pygame.event.pump()

    @staticmethod
    def __gameOver():
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = CSJVSCXKGame()
    game.startGame()