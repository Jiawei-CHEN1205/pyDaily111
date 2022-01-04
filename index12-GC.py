##################### garbage recycle (GC)
import sys
import os
import psutil
import gc
####sys.getrefcount() 引用计数

print(gc.get_threshold()) #(700, 10, 10)触发的阈值 三代
a = []
print(sys.getrefcount(a))
#2 说明使用a的地方有两个 第一个是建立处 第二个是打印处
#但是print结束后 还要给getrefcount减一 释放打印的那一次
b = a
c = b
d = c
a = a #自己调用自己不算一次
print(sys.getrefcount(a)) #5次
# 引用计数为0 就释放了

##############
# 循环引用导致内存泄露，注定python还将引入新的回收机制。(标记清除和分代收集)



# pid指的是运行这个python文件时的进程编号，
# 然后由编号获得进程对象，再获得对象运行是所占内存大小（单位：字节）
# 最后转换为MB
def showMemSize(tag):
    pid = os.getpid() #获取进程pid
    p = psutil.Process(pid) # 获取进程对象
    info = p.memory_full_info() # 获取进程信息
    memory  = info.uss/1024/1024 # 转换为MB
    print('{} memory used:{} MB' .format(tag,memory))
    pass

# 验证循环引用的情况
def func():
    showMemSize('初始化')
    a1 = [i for i in range(100000)]
    b1 = [i for i in range(100000)]
    a1.append(b1)
    b1.append(a1)
    showMemSize('创建列表对象a1,b1后')
    pass

func()
gc.collect() #手动释放内存
showMemSize('完成后')

a = 148 #小整数
b = 148
print(id(a))
print(id(b))
c = 148
del a
del b
print(id(c))




























