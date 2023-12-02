"""游戏暂停"""

import pygame

class GamePauseWindow():
    """游戏暂停界面"""
    def __init__(self, classMain):
        pygame.font.init()
        self.fontGameInfo = pygame.font.SysFont('Helvetica', 20)
        self.fontGameTitle = pygame.font.SysFont('Franklin Gothic', 30)
        self.fontAbout = pygame.font.SysFont('Helvetica', 15)
        self.window = classMain.window
        pygame.draw.rect(self.window, (0, 0, 0), (50, 50, 500, 300))
        """ 游戏分数 """
        self.textScores = self.fontGameInfo.render("Game Scores : " + str(classMain.scores), True, (255, 236, 0))
        self.window.blit(self.textScores, (75,70))
        """ 总投放鸡汤数 """
        self.textThrowTimes = self.fontGameInfo.render("Throw Times : " + str(classMain.throwTimes), True, (255, 236, 0))
        self.window.blit(self.textThrowTimes, (75,100))
        """ 命中率 """
        self.textRate = self.fontGameInfo.render("Hit Rate : " + self.hitRate(classMain.scores, classMain.throwTimes), True, (255, 236, 0))
        self.window.blit(self.textRate, (75,130))
        """ 关于 """
        self.textAbout1 = self.fontGameTitle.render("CSJ VS CXK", True, (255, 225, 225))
        self.window.blit(self.textAbout1, (230,160))
        self.textAbout2 = self.fontAbout.render("Developer: SPGLP55(LSL01)", True, (225, 225, 225))
        self.window.blit(self.textAbout2, (75,200))
        #self.textAbout3 = self.fontAbout.render("本游戏是一款基于 GPL 协议进行开源的 Python 语言小游戏，使用 Pygame 进行构造。开发工具为 VSCODE", True, (255, 225, 225))
        #self.window.blit(self.textAbout3,(50,270))
        self.textAbout4 = self.fontAbout.render("This is a Python language video game based on the GPL license and open source. ", True, (255, 225, 225))
        self.window.blit(self.textAbout4, (75,220))
        self.textAbout4_1 = self.fontAbout.render("Buliding with Pygame. Program tool is VSCODE.", True, (255, 225, 225))
        self.window.blit(self.textAbout4_1, (75,240))
        self.textAbout5 = self.fontAbout.render("Version: INDEV", True, (255, 225, 225))
        self.window.blit(self.textAbout5, (75,260))
        self.textAbout6 = self.fontAbout.render("Press P back to game", True,  (255, 225, 225))
        self.window.blit(self.textAbout6, (75,300))

    """
    hitRate(int, int)
    作用：计算并返回命中率(Hit Rate)为 String 类型(XX.XX%)
    参数：scores - 分数；throwTimes - 投掷次数
    """
    def hitRate(self, scores, throwTimes):
        if throwTimes == 0:
            return "0.0%"
        else:
            return str((scores / throwTimes) * 100) + "%"


    '''
    def windowListener(self):
        pressedKey = pygame.key.get_pressed()
        if pressedKey[pygame.K_p]:
            #super().screenSet()
            #super().gameIsPause = False
            self.setPauseStatus(False)
        pygame.event.pump()
    '''


    '''
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
    '''