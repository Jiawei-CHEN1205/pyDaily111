# import Modeltest #导入模块 导入所有 
# 注意要在同一个文件目录下才能直接这么调用
from Modeltest import *
from Modeltest import printInfo
# 或者导入一部分：
# from Modeltest import HappyBirthday

# #########  模块的制作、发布、安装  ##############
# 模块的定义：
# 在py中，一个.py文件就是一个模块
# 作用：
# 可以有逻辑的组织py代码
# 以库的形式去封装功能，非常方便调用
# 可以定义：函数、类、变量 也可以包括可执行的代码
# 注意：不同的模块可以定义相同的变量名，但是每个模块的变量名作用域只在本模块中

# 模块的分类：
# 内置模块  自定义的模块  第三方的模块

# （1）、Python文件都可以作为一个模块，模块的名字就是文件的名字。 
# 比如创建一个Modeltest.py文件，文件中创建一个add函数。Modeltest.py就是一个模块。

# Modeltest.HappyBirthday('陈家苇') #注意 依据导入方式的不同 选择不同的调用函数的模式
# 有的时候是 模块名.函数名() , 有的时候是直接 函数名() 
HappyBirthday('苇子')
# 为了避免直接把原来模块中的东西直接打印之类的（而是只取核心的函数功能之类的来调用），
# 需要使用到一个__name__的变量（魔术变量）

# 在原来的模块文件中加入if __name__ == '__main__':XXXXX 来限制内容


# print(Modeltest.differ(50,18))
# print(Modeltest.printInfo())


print(differ(23,11))
print(printInfo())
# 我发现在写 printInfo() 这句话的时候 文件开头部分会自动为我补全 from Modeltest import printInfo































































