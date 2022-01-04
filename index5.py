########全局变量 和 局部变量
#全局变量：
pro = '计算机系统'
#当全局变量（外部）和局部变量（函数内部）的名字定义的相同的时候，优先使用函数内部的变量（级别高）


#局部变量 只在函数内部使用的变量 属于内部定义 不同的函数可以定义“名字”相同的局部变量
#局部变量：为了临时保存数据 需要在函数内定义来进行存储
def printInfo():
    name1 = 'Randson'  #name1是局部变量
    print('{}' .format(name1))
    print('他的职业是：{}' .format(pro))
    pass
printInfo() #他的职业是：计算机系统


#在函数内容想要把某个定义的变量修改为全局变量，使用global关键字命令来声明：
def changeGlobal():
    global pro
    pro = '自动化测试'
    pass

changeGlobal() #别忘了运行一下函数 函数功能才能奏效
print(pro)

printInfo()  #他的职业是：自动化测试 #pro已经从 计算机系统 变成了 自动化测试


#引用
#用堆栈概念理解类似指针 a=1，相当于把a的标签指向1这个数据对应的地址
a=1
def findAddr(x):
    print('x的地址是：{}' .format(id(x)))
    pass

print('a的地址是：{}'.format(id(a)))
findAddr(a)
# a的地址是：140735192749088
# x的地址是：140735192749088
#地址是一样的 传的是对象的引用
#和C语言不一样，C语言分为 值传递，地址传递，引用传递，而Python中，值是靠引用来传递的
#python有新的值，不改变原内存，而是开辟一个新内存放新的值，然后把变量和新的内存挂钩，和C的区别似乎是：C的一个固定内存的内容是可以改变的
def findAddr1(x):
    print('x的地址是：{}' .format(id(x)))
    x=2
    print('x的修改后的地址是：{}' .format(id(x)))
    print('x=%d' %x)
    pass

print('a的地址是：{}'.format(id(a)))
findAddr1(a)
print('a=%d' %a)
# a的地址是：140735192749088
# x的地址是：140735192749088
# x的修改后的地址是：140735192749120
# x=2
# a=1
#a传递给x之后，两个指向同一个地址，之后对x修改，赋值2，如果二者是指向地址不变，只是地址对应的内容变了，
#那么x应该地址不变，但是实际打印之后发现变了，这就说明，是x指向了一个新的内存空间，也就是2对应的内存空间，但是a对应的不变，此外a是个全局变量，不改变；


#上述是不可变类型int   下举例可变类型，如列表list
li = []
def testRenc(parms):
    li.append([1,2,3,4,5])
    print(id(parms))
    print('内部的parms{}'.format(parms))
    pass

print(li)
print(id(li)) #原始li地址
testRenc(li) #将li 传递给parms,然后用append功能修改了值，函数体内的语句可输出新的地址
print('外部的变量{}'.format(li))
# 2317928456776
# 2317928456776
# 内部的parms[[1, 2, 3, 4, 5]]
# 外部的变量[[1, 2, 3, 4, 5]]
#当全局变量为可变数据类型时，局部函数可以改变其地址所对应的数值，而不改变其地址，所以li的值改变了，其地址没有变

#小结：1、在Python中，万物皆对象，在函数调用的时候，实参传递的就是对象的引用；
# 2、了解原理之后，可以更好的把控 在函数内部的处理，是否会影响到函数外部数据的变化；
# 3、参数传递是通过对象来完成的！！！

################################
######匿名函数
#语法：
# lambda 参数1、参数2、参数3:表达式
#特点
#使用lambda关键字去创建函数
#匿名函数冒号后面的表达式 有且只有一个 注意 是表达式 不是语句
#匿名函数自带return 而这个return的结果就是表达式计算后的结果

# lambda x,y:x+y

M = lambda x,y:x+y
#通过变量去调用匿名函数
#M(23,19)
print(M(23,19))

# 这个函数相当于下面的加和函数：
def sumSum(x,y):
    return(x+y)
    pass
print(sumSum(23,19))


#乘法举例：
re = lambda a,b,c:a*b*c #好简洁！
print(re(12,34,2))

####三元运算 & lambda
# if a:
#     b
#     pass
# else:
#     c
#     pass

#等效于：
# b if a else c

# 举例 
age = 25
print('可以参军' if age > 18 else '继续上学')

# lambda的运用 找大的值
funCompare = lambda x,y: x if x>y else y
print(funCompare(12,2))

#还可以这样调用
rs = (lambda x,y: x if x>y else y)(19,16) #后面括号里的（19,16）相当于赋了参数
print(rs)

#####lambda的缺点：只能单个表达式，只能实现简单逻辑，复杂的要用def

###################################
##### 递归函数 在函数内部调用自己 必须满足一个结束的条件才行
##求阶乘n!
##1、用循环的方式实现：
def jiecheng(n):
    result = 1
    for item in range(1,n+1):
        result *= item
        pass
    return result
    pass
print('5!={}'.format(jiecheng(5)))

##2、用递归实现：
def selfJc(n):
    if n == 1:
        return 1 ###关键的结束位置
        pass
    else:
        return n*selfJc(n-1)
    pass

##递归调用：
print('8!={}'.format(selfJc(8)))

######递归案例 模拟实现 树形结构的遍历
import os #引入文件操作模块
def findFile(file_Path):
    listRs = os.listdir(file_Path)#得到该路径下所有的文件夹 os.listdir()
    for fileItem in listRs:
        full_path = os.path.join(file_Path,fileItem) #获取完整的文件路径
        if os.path.isdir(full_path): #判断是否是一个文件夹
            findFile(full_path) #如果是一个文件夹，再次去递归
        else:
            print(fileItem)
            pass
        pass
#调用搜索文件夹对象
# findFile('C:\\1--HITsz_files\\2--香港新加坡申请-DIY')








