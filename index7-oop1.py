########定义 类 和 对象
# class 三个部分： 类名--属性--方法

# class 类名:
#     属性
#     方法

class Person:  # 创建类class
    nameP = '小米' #类属性 与“实例属性”区别
    ageP = 20
    def __init__(self) -> None:
        self.hobby = '打篮球'  #实例属性
        pass
#实例属性，是在方法内部定义的（通过self.变量名）来定义的，分配内存不同
    def eat(self):  #定义行为（方法）
        print('大口吃饭')
        pass
    def run(self):  #定义行为
        print('跑跑跑')
        pass
    # pass 


# 创建对象object：
# 对象名 = 类名()
xm = Person()
xm.eat() #调用函数 
# 实例方法 调用，是在类的内部定义的，使用def，第一个默认参数是self(占位的，名字标识可以是其他的，但是这个位置必须被占用)
print('小米的年龄:{}'.format(xm.ageP))

xl = Person()
print(xl.hobby) #调用了实例属性 

######################
### __init__方法：
class Animal(object): #创建类 动物
    def eat(self): #实例方法
        print('吃饭啊')
        pass
    def __init__(self) -> None: #初始化方法，实例化对象的时候自动调用，完成一些初始化设置。
        self.name = '旺财'
        self.color = '黄色'
        self.age = 1
    pass

cat = Animal() #对象cat
print(cat.color,cat.age) #默认的值 定义对象的时候就有了

cat.color = '白色' #追加/修改 实例属性，因为加了实例名，所以是实例的私有属性，而不是直接定义在类里面的“类属性”
cat.age = 3  #追加/修改 实例属性
print(cat.color,cat.age) #修改之后的  但原来的类里面的这些颜色年龄之类的不变，因此如果新建一个对象dog，那么这个对象的属性都是类里面默认的，而不是cat修改之后的
#如果n个对象，写n次添加属性，太麻烦 ，因此使用__init__方法：
#通过__init()__定义属性的值，你对属性值修改，只会对这一个对象生效

dogg = Animal() #第二个对象dogg
print(dogg.color) # 输出的是默认的 黄色

##############
## init 传参：
class Animal111(object): #创建类 动物
    def __init__(self,param1,param2,param3) -> None: #param1,param2,param3 传参
        self.name = param1
        self.color = param2
        self.age = param3
        pass
    def act(self,food):
        #行为
        print(self.name+'喜欢吃'+food)
        pass
    def coco(a): #特意把self换了个字母a
        print('a的头发颜色:%s' %a.color) 
        #a.color = 上面的self.color 也就是param2
    pass

cat111 = Animal111('张三','黄头发',19) # 对应三个param参数 定义对象的的时候就传入了参数
print(cat111.name,cat111.color,cat111.age)

cat112 = Animal111('李四','红头发',27) # 对应三个param参数
print(cat112.name,cat112.color,cat112.age)

cat111.act('香蕉') #返回： 张三喜欢吃香蕉
cat112.act('橘子') #李四喜欢吃橘子

cat111.coco() #a的颜色:黄头发

# 总结__init__
# 1、py自带的内置函数 具有特殊的函数 使用双下划线包起来的【魔术方法】
# 2、是一个初始化的方法 用来定义实例属性 和 初始化数据的 在创建对象时自动调用
# 3、利用传参的机制可以让我们定义功能更加强大并且方便的 类

################################
## 理解“self”
# self和对象指向同一个内存地址，可以认为self就是对象的引用。


class Idclss(object): #类
    def Idprint(self):
        print('地址是%s' %id(self))
        pass
    def eatFruit(self,name,food):
        print('%s喜欢吃%s' %(name,food))
        pass
    pass

xwID = Idclss() #对象
print('xw的地址是%s' %id(xwID)) # 打印这个对象的地址
xwID.Idprint() #调用函数
# xw的地址是2586786346600  两个地址一样的
#     地址是2586786346600

#所谓的self，可以理解为对象自己 对象就是方法的第一个参数“self”
xwID.eatFruit('小王','椰子') #self是xwID, name是小王,food是椰子 只需要传后面两个参数
#self相当于this关键字

# self总结：
# self 只有在类中定义实例方法的时候才有意义 在调用的时候不必传入"self" 而是解释器自动去指向
# self这个单词 约定俗成而已 也可以换其他单词
# self 指的是 类实例对象本身 例如xwID cat111


############################
## 魔法方法：
# 在python中，有一些内置好的特定的方法，方法名是“__xxx__”,
# 在进行特定的操作时会自动被调用，这些方法称之为魔法方法


# __str__:在将对象转换成字符串 str(对象) 测试的时候，打印对象的信息

class Magic1():
    def __init__(self,name,food,hobby) -> None:
        print('-------init执行--------')
        self.name = name
        self.food = food
        self.hobby = hobby
        pass
    def __str__(self) -> str:
        return '%s喜欢吃%s，爱好是%s' %(self.name,self.food,self.hobby)
        pass
    def __new__(cls, *args, **kwargs):
        '''创建对象实例的方法 每调用一次就会生成一个新的对象 cls就是类'''
        print('-------new------函数优先于init函数执行-----')
        return object.__new__(cls)
        # 没有上面这句话return 就没有把对象创建成功 真正创建对象实例 
        # 平时不写 使用的是默认的new函数 而这里我们显式的使用了new 那就必须return这个对象 不然就没有创建成功
        # 场景：可以控制创建对象的一些属性限定 经常用来做单例模式的时候来使用
        pass

#实例化对象：
MagicA = Magic1('大白老师','玉米','羽毛球')
print(MagicA) #改变了print的功能，不然原来print的内容是类似：<__main__.Animal111 object at 0x000001DD1CFB0550>
# 大白老师喜欢吃玉米，爱好是羽毛球
# __str__可以自定义打印输出的效果

######################
# __new__方法：真正创建并返回一个实例对象，调用了一次，就会得到一个对象。

# __init__和 __new__的区别：
#  __new__方法 必须要return返回实例 否则对象创建不成功
# __init__ 用来做数据属性的初始化工作 也可以认为是实例的构造方法 接受类的实例self 并对其进行构造
# __new__ 至少有一个参数是cls 代表要实例化的类 此参数在实例化时由解释器自动提供
# new 函数 分配空间 优先于init函数执行











