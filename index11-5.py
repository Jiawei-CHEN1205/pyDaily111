# 模块介绍
# import 导入模块 
# 比如我们导入一个时间模块time，获取当前时间。 
# import time #全部导入 
# from time import * #也表示全部导入
# print(time.ctime())


import shutil 

# 调用模块的方法，格式：模块名.函数名，这样调用可以防止不同模块中有同名方法导致错误。
# time 模块名 、ctime 函数名
# 首次导入模块时候的工作（内置）：
# 1、打开模块文件（.py）
# 2 执行对应文件 将执行过程中产生的名字丢到模块的名称空间
# 3 在程序中会有一个模块的名称指向模块的名称空间去

#############################################################
# from  ... import ...,...
# 一个模块可能会存在很多函数，如果只想导入其中几个函数，可以使用from xx import xx 方式导入
# 1 以模块为准创造一个模块的名称空间
# 2 执行模块对应的文件，将执行过程中产生的名字丢到模块的名称空间
# 3 在当前执行文件的名称空间中会拿到一个名字，该名字直接指向模块中的某一个名字
# from time import ctime, time
# print(ctime())  # 优点：这里不需要加前缀了/加了time.反而会报错，直接ctime  而不用time.ctime()

# 不全部导入，可以防止将自己写的同名函数覆盖

#############################################################
# 另外可以给模块起别名
# 有时候导入的模块名称很长，调用的时候很不方便，这个使用就可以用as给这个模块取别名。
import time as myTime # 原来的time 名称将会失效
print(myTime.ctime())
print(myTime.strftime('%Y-%m-%d %H:%M:%S',myTime.localtime())) # 格式化输出时间格式 2021-12-05 20:31:29

########################################
## os 模块操作
import os
# os.rename('test1121.txt','poem 1121.txt') # 重命名文件，两个参数：src dst
# os.remove('thesis1121_备份.txt') #删除文件 一般会做一下存在与否的判断
#创建文件夹
# os.mkdir('pyDaily') #当前目录下 创建文件夹
# os.rmdir('pyDaily') # 删除文件夹,且必须是空目录（文件夹里有子文件的话删不掉 报错）


# 删除非空目录，需要用 shutil 模块 _____   import shutil
# shutil.rmtree('d:/C--Notebooks/1--GAP')


# 更改路径为 d盘：  
# 创建文件夹，甚至可以创建级联文件夹 多级目录（mkdir前提是上一级已经存在了） 
# 删除也可以级联的
# os.mkdir('d:/B--Software_daily')
# os.mkdir('d:/B--Software_daily/crx_google')
# os.rmdir('d:/B--Software_daily/crx_google')
# os.mkdir('d:/D--Other Document')


# 直接创建一组级联目录 用makedirs()
# os.makedirs('d:/C--Notebooks/1--GAP/referMy')
# os.makedirs('d:/C--Notebooks/1--GAP/dataMy')
# os.makedirs('d:/C--Notebooks/1--GAP/paperMy')

# 获取当前的目录：
print(os.getcwd()) # D:\A--HITsz_files\4--learnPY

# ### 路径的拼接
# 打印的是os 这模块的路径：
print(os.path)
# <module 'ntpath' from 'C:\\Users\\Byzcj1205\\AppData\\Local\\Programs\\Python\\Python37\\lib\\ntpath.py'>
joinPath = os.path.join(os.getcwd(),'pyDaily') # 用 , 拼接
print(joinPath)
# tips：拼接路径可以避免hardcode，还可动态生成文件夹
# 在获取你这个路径之后 可以生成路径/树1,如果后面写程序使用的人多的话,路径要获取,不可以写死

# 获取Python中的目录列表 只打印一级数据  返回一个Python列表
listDir = os.listdir('d:/')
# print(listDir) # 这种打印是个列表 带引号的那种 不如使用一个for循环来打印：
for DirName in listDir:
    print(DirName)
    pass

# # 使用现代版的写法：
# with os.scandir('d:/') as entities: # entity 实体
#     for entity in entities:
#         print(entity.name)
# # 获取文件和目录属性(如文件大小和修改日期)，os.scandir() 是首选的方法
print('###############################')

basePath = 'd:/A--HITsz_files/4--learnPY'
for entity in os.listdir(basePath):
    # if os.path.isfile(os.path.join(basePath,entity)): # isfile 如果是文件 则打印 也就是文件夹打印
    #     print(entity)
    if os.path.isdir(os.path.join(basePath,entity)): #isdir  只打印“文件夹”对象的名字 其他的诸如docx之类的不打印
        print(entity)



















































































