############# 飞机大战 应用
import pygame
# print('导入游戏库成功！！！')
import random

from pygame.locals import * # *号表示的是导入全部

'''
1、定义一个类 HeroPlane
实现飞机的显示，并且可以控制飞机的移动【面向对象】
'''
class HeroPlane(object):
    def __init__(self,screen) -> None:
        '''传入参数 screen = 主窗体对象'''
        # 玩家飞机的默认位置
        self.x = 100
        self.y = 450
        # 设置要显示的内容的窗口
        self.screen = screen # 之后实例化的时候 就是主函数main里面的screen1 背景窗口 我特意加了个1表示区分形参和实参
        # 生成飞机的图片对象
        self.imageName = 'C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/hero1.jpg'
        self.image = pygame.image.load(self.imageName)
        self.image = pygame.transform.scale(self.image,(50,50))# 改变图片的大小 这句话可以忽略 我本身设计的图片就是50*50 建议用画图工具调整大小
        
        # 存放子弹的列表
        self.listBullet = []
        
        pass
        # 接下来五个函数 对应五个功能键 上下左右和空格（发射子弹）：
    def MoveLeft(self): # 左移函数
        if self.x >= 10:
            self.x -= 10 # 左移 横坐标减 步长为10
            pass
        pass
    def MoveRight(self):
        if self.x <= 340: #340 = 400-50-10
            self.x += 10 # 右移 横坐标+
            pass
        pass
    def MoveUp(self):
        if self.y >= 10:
            self.y -= 10 # 上移
            pass
        pass
    def MoveDown(self):
        if self.y <= 440:
            self.y += 10 # 下移
            pass
        pass

    # 第五个函数，发射子弹 # 注意这个功能函数是写在飞机这个类里面的 之后供给空格调用
    def Shoot(self): 
        # 创建一个新的子弹对象（实例化）
        newBullet = Bullet(self.x,self.y,self.screen) 
        #前面两个坐标参数，即飞机的坐标self.x和self.y，第三个参数依然是screen主窗口
        
        # 追加子弹对象append列表，因此列表中的元素都是一个个的子弹对象，每次调用一次shoot 都会增加一个子弹实体：
        self.listBullet.append(newBullet)
        pass
    # 在主窗口显示飞机和子弹
    def DisplayHero(self): 
        self.screen.blit(self.image,(self.x,self.y)) #blit第一个参数是飞机图片名称，后面括号内的是坐标参数
        # 完善子弹的显示逻辑：
        DelBulletList = []
        # 1、越界的子弹先保存到DelBulletList里面
        for item in self.listBullet: 
            if item.Judge(): #list中放置的是子弹对象,因此可以访问这个函数judge 返回的bool类型做越界与否的判断
                DelBulletList.append(item)
                pass
            pass
        # 2、再次遍历 删除越界的子弹 (因为正在遍历的时候是不能删除的 前述第1步)
        # 删除子弹的好处 可以节约内存
        for k in DelBulletList:
            self.listBullet.remove(k) # 原列表listBullet里面删除掉越界的子弹，也就是DelBulletList里面的子弹
            pass
        # 3、删除了之后 可以开始展示有效的子弹的位置了
        for bullet in self.listBullet:
            bullet.DisplayBullet() # 子弹位置
            bullet.MoveBullet() # 让子弹进行移动，下次再刷新显示的时候，就可以看到修改后的子弹的位置了
        # 关键是将子弹显示移动函数shoot和dispaly放在了飞机显示移动函数里，
        # 而飞机显示移动函数恰好在main函数的while无限循环结构里，
        # 从而达到了子弹轨迹的形成
        pass

'''
2、下一步，加入子弹类(hero的子弹)
'''
class Bullet(object):
    def __init__(self,x,y,screen) -> None:
        '''
        x:飞机横坐标 y:飞机纵坐标 screen:主窗口
        '''
        self.x = x+17  # 子弹的坐标self.x是相对于飞机的坐标位置而定义的
        self.y = y-15
        self.screen = screen # 这里的screen之类的都是形式参数
        # 导入子弹的图片18*30大小
        # self.image = pygame.image.load('C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/bullet2.jpg')
        self.image = pygame.image.load('C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/feiji/bullet_teacher.png')
        pass
    def DisplayBullet(self): # 显示子弹
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def MoveBullet(self): # 子弹的移动 注意子弹只有y方向的移动
        self.y -= 3 # 坐标的变化 向上发射 数值大小影响到子弹的速度
        pass
    
    def Judge(self): # 判断子弹是否越界 返回bool类型
        if self.y <0:
            return True
        else:
            return False
    pass







'''
3、普通函数 实现键盘检测
HeroObj = 实例化的玩家飞机对象参数'''
def Key_control(HeroObj): #HeroObj是个形参而已
    # 获取键盘事件 上下左右和空格（发射子弹）
    evenList = pygame.event.get() 
    for event in evenList:
        if event.type == QUIT:
            print('按下了退出')
            exit()
            pass
        elif event.type == KEYDOWN:# KEYDOWN按下按键的关键字event.type
            if event.key == K_a or event.key == K_LEFT: # 按下left 关键字是event.key 而不是 event.type
                print('left')
                HeroObj.MoveLeft() #调用左移函数，左移函数的定义在飞机类里面
                pass
            elif event.key == K_d or event.key == K_RIGHT:# 按下right 
                print('right')
                HeroObj.MoveRight() #调用右移函数
                pass
            elif event.key == K_w or event.key == K_UP:
                print('up')
                HeroObj.MoveUp() #调用向上函数
                pass
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                HeroObj.MoveDown() #调用向下函数
                pass
            elif event.key == K_SPACE:
                print('blankspace 发射子弹')
                # 按空格键发射子弹
                HeroObj.Shoot() # 调用shoot函数（定义在飞机里面）
            pass
        pass


'''
5、创建敌机类enemy

'''
class EnemyPlane(HeroPlane):
    def __init__(self,screen) -> None:
        '''传入参数 screen = 主窗体对象'''
        # 敌人飞机的默认位置
        self.x = 100
        self.y = 100
        # 设置要显示的内容的窗口
        self.screen = screen # 实例时 是screen1 背景窗口
        # 生成敌人飞机的图片对象
        self.imageName = 'C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/enemy1.jpg'
        self.image = pygame.image.load(self.imageName)
        self.image = pygame.transform.scale(self.image,(50,50))# 改变图片的大小 这句话可以忽略 我本身设计的图片就是50*50 建议用画图工具调整大小
        
        # 存放敌机子弹的列表
        self.listBullet = []
        pass
    
    # 敌机的发射子弹 随机发射子弹
    def Shoot1(self): 
        num = random.randint(1,120)
        if num == 13:
            # 如果随机数是3，就创建一个新的敌机的子弹对象（实例化）
            newBullet1 = EnemyBullet(self.x,self.y,self.screen) 
            # 追加敌机的子弹对象append列表
            self.listBullet.append(newBullet1)
        pass
    # 在主窗口显示enemy和子弹
    def DisplayEnemy(self):
        super().DisplayHero() #表示继承父类的display函数
    # 敌机的移动控制(随机)
    def EnemyMove(self):
        x_0 = random.randint(0,7)
        y_0 = random.randint(0,1)
        self.x = x_0 * 50
        self.y = y_0 * 50
       
        pass
    
    pass

'''
6、敌机的子弹类
'''

class EnemyBullet():
    def __init__(self,x,y,screen) -> None:
        '''
        x:敌机横坐标 y:飞机纵坐标 screen:主窗口
        '''
        self.x = x+18  # 子弹的坐标self.x是相对于敌机的坐标位置而定义的
        self.y = y+21+50
        self.screen = screen # 这里的screen之类的都是形式参数
        # # 导入子弹的图片18*30大小
        # self.image = pygame.image.load('C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/bullet3.jpg')
        # 导入子弹的图片9*21大小
        self.image = pygame.image.load('C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/feiji/bullet1_teacher.png')
        pass
    def DisplayBullet(self): # 显示子弹
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def MoveBullet(self): # 子弹的移动 注意子弹只有y方向的移动
        self.y += 3 # 坐标的变化 向下发射
        pass
    
    def Judge(self): # 判断子弹是否越界 返回bool类型
        if self.y >(500-21):
            return True
        else:
            return False
    
    
    pass




'''4、主函数部分 包括了定义背景图片、背景音乐 实例化飞机对象等等功能'''

def main():
    # 首先创建一个主窗口screen1 用来显示内容
    screen1 = pygame.display.set_mode((400,500)) #(width,height) 注意有两层括号
    # 创建一个背景图片对象 一般是图片大小和你创建的窗口大小一致
    background = pygame.image.load(r'C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/background1.png')

    # 设置一个title
    pygame.display.set_caption('飞机大战小游戏')
    # 添加背景音乐 使用mixer功能里的music
    pygame.mixer.init()
    pygame.mixer.music.load('C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/music.mp3')
    pygame.mixer.music.set_volume(0.2) # 设置音量 可以不设置 用默认的大小
    pygame.mixer.music.play(-1) #-1表示无限循环
              
    # 创建一个飞机对象Hero1 需要传入的参数是定义__init里的screen 实参是screen1
    Hero1 = HeroPlane(screen1) 
    # 敌机一个敌机实例对象enemy1
    enemy1 = EnemyPlane(screen1)

    while True: # 一直循环 刷新页面
        # 设定要显示的内容
        screen1.blit(background,(0,0)) #居中显示(0,0)背景图片
        # 显示玩家飞机的图片
        Hero1.DisplayHero() #调用 按照设定的x,y，显示玩家的位置

        # 获取键盘事件
        Key_control(Hero1) #传入实际的对象Hero1
        # 显示敌机飞机的图片
        enemy1.DisplayEnemy() #调用 按照设定的x,y，显示敌机的位置
        # 敌机发射子弹
        enemy1.Shoot1()
        #移动敌机:
        newEnemy = random.randint(1,120)
        if newEnemy == 4:
            enemy1.EnemyMove()
            pass
        # 更新显示的内容
        pygame.display.update()
        pygame.time.Clock().tick(80)
        # 知道是循环的原因，又知道循环是为了检测键盘事件，所以死循环是不可能省略的了，
        # 但是我们可以想办法，让循环次数变少，而且变少后不影响程序对键盘的检测，
        # 比如我们让程序员秒内只检测键盘5次，这样的计算量就会大幅减少，而且和一条语句就能解决问题
        pass
    pass

if __name__ == "__main__":  # 这个后续会讲
    main()
# main()








# 面向过程的代码
# def main():
#     # 首先创建一个窗口 用来显示内容
#     screen = pygame.display.set_mode((400,500)) #(width,height) 注意有两层括号
#     # 创建一个背景图片对象
#     background = pygame.image.load(r'C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/background1.png')
#     # 设置一个title
#     pygame.display.set_caption('飞机大战小游戏')
#     # 添加背景音乐
#     pygame.mixer.init()
#     pygame.mixer.music.load('C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/music.mp3')
#     pygame.mixer.music.set_volume(0.2) # 设置音量 可以不设置 用默认的大小
#     pygame.mixer.music.play(-1) #-1表示无限循环
    
#     # 先载入玩家的飞机图片hero
#     hero = pygame.image.load('C:/A--HITsz_files/4--learnPY/qiuzhi_feiji/hero1.jpg')
#     hero = pygame.transform.scale(hero,(50,50))# 改变图片的大小
#     # 初始化玩家的位置：
#     x,y = 0,0 # 左上角位置 (0,0)
    
#     Hero1 = HeroPlane(screen) # 创建一个飞机对象Hero1 需要传入的参数是init里的screen


#     while True:
#         # 设定要显示的内容
#         screen.blit(background,(0,0)) #居中显示(0,0)
#         # 显示玩家的图片
#         screen.blit(hero,(x,y)) #按照设定的x,y，显示玩家的位置
#         # 获取键盘事件
#         evenList = pygame.event.get() 
#         for event in evenList:
#             if event.type == QUIT:
#                 print('按下了退出')
#                 exit()
#                 pass
#             elif event.type == KEYDOWN:# KEYDOWN按下按键的关键字
#                 if event.key == K_a or event.key == K_LEFT: # 按下left 
#                     print('left')
#                     if x >= 5:
#                         x -= 5 # 左移 横坐标减
#                         pass
#                     pass
#                 elif event.key == K_d or event.key == K_RIGHT:# 按下right 
#                     print('right')
#                     if x <= 345:
#                         x += 5
#                     pass
#                 elif event.key == K_w or event.key == K_UP:
#                     print('up')
#                     if y >= 5:
#                         y -= 5
#                         pass
#                     pass
#                 elif event.key == K_s or event.key == K_DOWN:
#                     print('down')
#                     if y <= 445:
#                         y += 5
#                         pass
#                     pass
#                 elif event.key == K_SPACE:
#                     print('blankspace')
#                     pass
#                 pass
#             pass
#         # 更新显示的内容
#         pygame.display.update()
#         pass
#     pass

# if __name__ == "__main__":  # 这个后续会讲
#     main()
# # main()






































