import pygame

pygame.init()

screen = pygame.display.set_mode((480,700))
#绘制背景图像
#1.加载背景图像
bg = pygame.image.load("./images/background.png")
#2.blit方法绘制图像
screen.blit(bg,(100,0))
#3.update 更新屏幕显示
pygame.display.update()
#游戏循环
while True:
    pass
pygame.quit()
