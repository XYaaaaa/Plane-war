import random
import pygame

#屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT+1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        

    def update(self):
        #在屏幕的垂直方向上移动
        self.rect.y += self.speed
#背景精灵类
class Background(GameSprite):
    
    def __init__(self,is_alt = False):

        #1.调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png",speed = 1)
        #2.判断是否是交替图像
        if is_alt:
            self.rect.y = -self.rect.height
    
    #游戏背景精灵
    def update(self):
        super().update() #调用父类的方法实现
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
#敌机精灵类
class Enemy(GameSprite):


    def  __init__(self):
        #1.调用父类方法，创建敌机精灵，指定敌机图片
        super().__init__("./images/enemy1.png",speed = 1)
        #2.指定敌机的初始随机速度
        self.speed = random.randint(1,5)

        #3.指定敌机的初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)

    def update(self):
        
        #1.调用父类方法，保持垂直方向的飞行
        super().update()
        #2.判断是否飞出屏幕，如果是，删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            #print("飞出屏幕")
            #kill方法可以将精灵从所有精灵组中移出，精灵会被自动销毁
            self.kill()

#英雄精灵类
class Hero(GameSprite):

    def __init__(self):

        #1.调用父类方法，设置image 和speed
        super().__init__("./images/me1.png", speed =0 ) 
        #2.英雄初始位置设置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        #3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        #英雄在水平方向移动
        self.rect.x += self.speed
        #控制英雄不能出屏幕
        if self.rect.x < 0:
            self.rect.x =0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right   

    def fire(self):
        for i in range(3):
       
            #1.创建子弹精灵
            bullet = Bullet()
            #2.设置精灵的位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            #3.将精灵添加到精灵组
            self.bullets.add(bullet)
#子弹精灵
class Bullet(GameSprite):
    def __init__(self):
        #调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet1.png", speed = -2)
        
    def update(self):
        #调用父类方法，让子弹沿垂直方向飞行
        super().update()
        #判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()


       

