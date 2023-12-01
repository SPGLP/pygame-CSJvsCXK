"游戏暂停"

import pygame
from GameWindow import CSJVSCXKGame

class GamePauseWindow(CSJVSCXKGame):
    def __init__(self):
        pygame.font.init()
        self.fontGameInfo = pygame.font.SysFont('宋体', 30)
        self.fontAbout = pygame.font.SysFont('宋体', 15)
        self.screenDisplay = pygame.display
        self.window = self.screenDisplay.set_mode((300, 400))
        self.screenDisplay.set_caption("游戏暂停")
        self.clock = pygame.time.Clock()
        self.textScores = self.fontGameInfo.render("当前得分：" + str(super().scores), True, (0, 0, 0))
        self.window.blit(self.textScores,(100,50))
        """ Add：总投放鸡汤数 """
        """ Add：命中率 """
        self.textAbout1 = self.fontAbout.render("CSJ VS CXK", True, (0, 0, 0))
        self.window.blit(self.textAbout1,(100,200))
        self.textAbout2 = self.fontAbout.render("作者(Developer): SPGLP55(LSL01)", True, (0, 0, 0))
        self.window.blit(self.textAbout2,(50,250))
        self.textAbout3 = self.fontAbout.render("本游戏是一款基于 GPL 协议进行开源的 Python 语言小游戏，使用 Pygame 进行构造。开发工具为 VSCODE", True, (0, 0, 0))
        self.window.blit(self.textAbout1,(50,270))
        self.textAbout4 = self.fontAbout.render("This is a Python language video game based on the GPL license and open source. Buliding with Pygame. Program tool is VSCODE.", True, (0, 0, 0))
        self.window.blit(self.textAbout1,(50,290))
        self.textAbout5 = self.fontAbout.render("版本(Version): INDEV", True, (0, 0, 0))
        self.window.blit(self.textAbout1,(50,310))
        self.textAbout5 = self.fontAbout.render("按 P 键继续游戏", True, (0, 0, 0))
        self.window.blit(self.textAbout1,(50,350))
        self.windowListener()
    
    def windowListener(self):
        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()
            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_p]:
                super().screenSet()
                #super().gameIsPause = False
            pygame.event.pump()
            pygame.display.update()