

import random

targetX = random.randint(0,9) # 目标位置
targetY = random.randint(0,9)

userX = random.randint(0,9) #用户初始位置 设计为随机的 也可以设置为固定值
userY = random.randint(0,9)
score = 0 # 得分纪录

while True:
    for itemX in range(0,10): # 上下 x 
        char = ""
        Outstr =""
        for itemY in range(0,10): # 左右 y
            if userX == targetX and userY == targetY:
                targetX = random.randint(0,9) # 匹配后 重新生成目标的位置 并得分加一
                targetY = random.randint(0,9)
                score += 1
                print("当前分数:%d" %score)
                pass
            if userX == itemX and userY == itemY:
                char = "#" # 用户的位置#
            elif targetX == itemX and targetY == itemY:
                char = "*" # 目标位置*
            else:
                char = "-" # 其余位置是-

            Outstr += char
            pass
        print(Outstr)
        pass


    move = input("请移动或退出：").upper() # 接受输入的字符
    if move == 's' or move == 'S':
        userX +=1 and userX < 9
        pass
    elif move == 'w' or move == 'W':
        userX -=1 and userX > 0
        pass
    elif move == 'a' or move == 'A':
        userY -=1 and userY > 0
        pass
    elif move == 'd' or move == 'D':
        userY +=1 and userY < 9
        pass
    elif move == 'quit' or move == 'QUIT': #退出
        break

# while 循环外： 
print("游戏结束，最终得分：{}分".format(score))


















