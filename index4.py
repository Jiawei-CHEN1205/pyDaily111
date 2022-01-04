#######lessson 4 函数基础

#1、定义函数def
# def 函数名():
#     函数体[...]

# def printInfo():
#     '''
#     这个函数是用来打印个人信息的
#     '''
#     #函数代码块
#     print('小明的身高是%f' %1.78)
#     print('小明的体重是%d' %125)
#     print('小明的爱好是%s' %'唱跳rap')
#     print('小明的专业是%s' %'计算机科学与技术')
#     pass
# #函数调用
# printInfo()


#############################
#输出不同人的信息 需要传入参数
def printInfo(name,height,weight,hobby,pro):
    print('%s的身高是%f' %(name,height))
    print('%s的体重是%d' %(name,weight))
    print('%s的爱好是%s' %(name,hobby))
    print('%s的专业是%s' %(name,pro))
    pass

#调用带参数的信息
printInfo('小李子',185,140,'打游戏','咨询师')
printInfo('Peter',176,130,'写代码','老师')


#############
#参数分类 ：必选参数、默认（缺省）参数、可选参数、关键字参数
#上述name，height之类的，是形式参数（形参），在定义的时候不占内存地址
#参数相当于函数的入口
#后面输入的'小李子'之类的，是实际参数（实参），占用内存地址

def sum1(a=20,b=30): #带默认参数；
    #也可以一个赋值，一个不赋值；调用的时候，没有默认值得那个参数必须传入实参
    print('加和值为：%d' %(a+b))
    pass

sum1() #使用默认参数
sum1(15)  #改了a

##可变参数 *表示（当参数个数不确定时，使用灵活)
def getComputer(*args):
    '''
    计算累加和
    param（参数）：args——可变长的参数类型
    return：
    
    '''
    #print(args)
    result = 0
    for item in args:
        result += item
        pass
    print('结果是：%d' %result)
    pass

getComputer(5,6,7,8,9)
getComputer(1,2,3)

#####关键字可变参数
# 用**来定义
#在函数体内 参数关键字是一个字典类型 key是一个字符串
def keyFunc(**kwargs):
    #kwargs_参数名称固定字典
    print(kwargs)
    pass


###########调用
# keyFunc(1,2,3) #不可以这样传 因为参数需要是字典

dictM = {'name':'Leo','age':35}
keyFunc(**dictM)  #注意两个*号必须带着

keyFunc(name='jack',age=26,pro='singer') #直接这样调用也可
keyFunc(**{'name':'cindy','age':24}) #或者这样调用，相当于把dictM那个写一起了


#混着用也可:
def complexFunc(*args,**kwargs):
    print(args)
    print(kwargs)
    pass
complexFunc(1,2,3,4,5,addr='深圳')
# 返回结果是两个，前面的args被识别为元组，后面的字典被识别为kwargs
# (1, 2, 3, 4, 5)
# {'addr': '深圳'}


####可选参数必须放到关键字可选参数之前，因此下面的例子是错的
# def testFunc(**kwargs,*args):
#     pass

#####可选参数：元组类型 一般用*args表示 (arguments)
####关键字可选参数：字典类型，一般用**kwargs表示 (kewwords arguments)


######################函数返回值
#函数内部有return 就可以返回实际的值 否则返回为空
#类型：可以返回任意类型 取决于return后面跟的类型
#用途：给调用方返回数据
#一个函数体内可以出现多个return关键字 但是只能返回一个实际的return
#在一个函数体内 执行了return意味着函数执行完成结束退出 之后的代码不会被执行

def sum2(a,b):
    res=a+b
    return res
    pass

print(sum2(10,30))  #40

res1=sum2(10,30)  #返回值赋给其他变量
print(res1) #40

# def calComputer(num):
#     result = 0
#     i=1
#     while i<=num:
#         result += i 
#         i+=1
#         pass
#     return result
#     pass

def calComputer(num):
    li=[]
    result = 0
    i=1
    while i<=num:
        result += i 
        i+=1
        # li.append(result)  #把每一步的加和结果放到列表里
        pass
    li.append(result)  #把加和结果放到列表里
    return li
    pass


#调用函数
value = calComputer(100)
print(type(value))  #result是int 所以返回就是int 其他类型同理
#后面改成return li 之后 返回的类型就是list了
print(value)



###################################
###嵌套调用

def fuc1():
    print('-----------func1 begin')
    print('-----------func1 body----------')
    print('-----------func1 end')
    pass

def fuc2():
    print('-----------func2 begin')
    fuc1() #嵌套调用
    print('-----------func2 end')
    pass

fuc2()













