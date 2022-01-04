####紫禁之巅
# 决战紫禁之巅有两个人物，西门吹雪以及叶孤城
# 属性：
# name 玩家的名字
# blood 玩家血量

# 方法：
# tong() 捅对方一刀,对方掉血10滴
# kanren() 砍对方一刀，对方掉血15滴
# medicine() 吃一颗药，补血10滴
# __str__ 打印玩家状态。

import time #导入时间包 
import random

#两个玩家是两个类[角色] 之后创建技能

class Role:
    def __init__(self,name,hp) -> None:
        '''
        name:名字
        hp:血量
        '''
        self.name = name
        self.hp = hp
        
        pass
    def tong(self,enemy): #捅一刀 吃药补血
        enemy.hp -= 10
        print('【%s】捅了【%s】一刀' %(self.name,enemy.name))
        pass
    def kanren(self,enemy):# 砍一刀 
        enemy.hp -= 15
        print('【%s】砍了【%s】一刀' %(self.name,enemy.name))
        pass
    def medicine(self):
        self.hp += 10
        print('【%s】补充血量10' %(self.name))
        pass
    def __str__(self) -> str:
        return '【%s】的剩余血量是%d' %(self.name,self.hp)
        # return '%s的剩余血量是%s' %(self.name,self.hp) 血量用%s %d 都可以
        pass

# 实例化两个人物对象
xmcx = Role('西门吹雪',100)
ygc = Role('叶孤城',100)


while True:
    # x2y_tong = random.randint(0,1)
    # y2x_tong = random.randint(0,1)

    # x2y_kan = random.randint(0,1)
    # y2x_kan = random.randint(0,1)

    # x_medi = random.randint(0,1)
    # y_medi = random.randint(0,1)

    GameMode = random.randint(1,6)

    if xmcx.hp <= 0 or ygc.hp <= 0:
            # 血量低于零 游戏结束
        print('游戏结束！')
        break
    # if x2y_tong == 1:
    if GameMode == 1:

        xmcx.tong(ygc) # 西门吹雪 捅了 叶孤城 一刀
        print(ygc) #打印玩家状态
        print(xmcx) #打印玩家状态
        print('---------------------')
        pass
    # elif y2x_tong ==1:
    elif GameMode == 2:

        ygc.tong(xmcx) # 叶孤城 捅了 西门吹雪 一刀
        print(ygc) #打印玩家状态
        print(xmcx) #打印玩家状态
        print('---------------------')
        pass
    # if x2y_kan == 1:
    elif GameMode == 3:

        xmcx.kanren(ygc)
        print(ygc) #打印玩家状态
        print(xmcx) #打印玩家状态
        print('---------------------')
        pass
    # elif y2x_kan == 1:
    elif GameMode == 4:

        ygc.kanren(xmcx)
        print(ygc) #打印玩家状态
        print(xmcx) #打印玩家状态
        print('---------------------')
        pass
    # if x_medi == 1:
    elif GameMode == 5:

        xmcx.medicine()
        print(ygc) #打印玩家状态
        print(xmcx) #打印玩家状态
        print('---------------------')
        pass
    # elif y_medi == 1:
    elif GameMode == 6:

        ygc.medicine()
        print(ygc) #打印玩家状态
        print(xmcx) #打印玩家状态
        print('---------------------')
        pass

    time.sleep(1) #每次循环休眠一秒钟
    pass








# ##################################################################

# ####紫禁之巅
# # 决战紫禁之巅有两个人物，西门吹雪以及叶孤城
# # 属性：
# # name 玩家的名字
# # blood 玩家血量

# # 方法：
# # tong() 捅对方一刀,对方掉血10滴
# # kanren() 砍对方一刀，对方掉血15滴
# # medicine() 吃一颗药，补血10滴
# # __str__ 打印玩家状态。

# import time #导入时间包 
# import random

# #两个玩家是两个类[角色] 之后创建技能

# class Role:
#     def __init__(self,name,hp) -> None:
#         '''
#         name:名字
#         hp:血量
#         '''
#         self.name = name
#         self.hp = hp
        
#         pass
#     def tong(self,enemy): #捅一刀 吃药补血
#         enemy.hp -= 10
#         print('【%s】捅了【%s】一刀' %(self.name,enemy.name))
#         pass
#     def kanren(self,enemy):# 砍一刀 
#         enemy.hp -= 15
#         print('【%s】砍了【%s】一刀' %(self.name,enemy.name))
#         pass
#     def medicine(self):
#         self.hp += 10
#         print('【%s】补充血量10' %(self.name))
#         pass
#     def __str__(self) -> str:
#         return '【%s】的剩余血量是%d' %(self.name,self.hp)
#         # return '%s的剩余血量是%s' %(self.name,self.hp) 血量用%s %d 都可以
#         pass

# # 实例化两个人物对象
# xmcx = Role('西门吹雪',100)
# ygc = Role('叶孤城',100)


# while True:
#     if xmcx.hp <= 0 or ygc.hp <= 0:
#         # 血量低于零 游戏结束
#         print('游戏结束！')
#         break
#     xmcx.tong(ygc) # 西门吹雪 捅了 叶孤城 一刀
#     print(ygc) #打印玩家状态
#     print(xmcx) #打印玩家状态
#     print('---------------------')
#     ygc.kanren(xmcx)
#     print(ygc) #打印玩家状态
#     print(xmcx) #打印玩家状态
#     print('---------------------')
#     xmcx.medicine()
#     print(ygc) #打印玩家状态
#     print(xmcx) #打印玩家状态
#     print('---------------------')

#     time.sleep(1) #每次循环休眠一秒钟
#     pass






















