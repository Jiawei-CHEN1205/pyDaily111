#################面向对象（下）
## 私有化属性：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问
# 1、把特定的一个属性隐藏起来 不想让类的外部进行直接调用
# 2、想保护这个属性 不想让属性的值随意改变
# 3、保护属性 不想让子类（派生类）去继承

class Person1:
    def __init__(self) -> None:
        self.__name = '栗子'# 加两个下划线 将此属性私有化 不能外部用 但是在类的内部可以访问
        self.age = 30
        pass    
    def __str__(self) -> str:
        return '{}的年龄是{}' .format(self.__name,self.age) # 在类的内部可以访问__name
        pass
        
xl = Person1()
# print(xl.__name)  # 这句话报错 没有定义__name
print(xl)      
class College(Person1):
    def PrintInfo(self):
        # print(self.__name) # 在子类中 也不能访问父类的私有属性
        print(self.age)
    pass

stu1 = College()
stu1.PrintInfo()
print(stu1)

########### 同理也有私有化方法 双下划线 def __eat(self):

#########################################################
## 单例模式
# 是一种常用的软件设计模式 目的：确保某一个类只有一个实例存在
# 如果希望在某个系统中 某个类只能出现一个实例对象的时候 那么这个单例对象就满足要求

# 创建一个单例对象 基于__new__去实现的【推荐的一种】

class DataBaseCls(object):
    def __new__(cls,*args,**kwargs):
        # cls._instance = cls.__new__(cls) 切忌这样使用 因为 我们不能使用自身的new方法，否则容易造成死循环
       
        if not hasattr(cls,'_instance'):  # 如果不存在 就开始创建
            #hasattr() 函数用于判断对象是否包含对应的属性
            cls._instance = super().__new__(cls,*args,**kwargs) #我们应该用父类的new方法
        return cls._instance
    # def __init__(self,name) -> None:
    #     self.name =name
    #     pass
    pass
db1 = DataBaseCls()
print(id(db1))
db2 = DataBaseCls()
print(id(db2))
db3 = DataBaseCls()
print(id(db3))
# 三个地址一样


class DataBaseCls2(object):
    def __new__(cls,*args,**kwargs):
        # cls._instance = cls.__new__(cls) 切忌这样使用 因为 我们不能使用自身的new方法，否则容易造成死循环
        cls._instance = super().__new__(cls,*args,**kwargs) #我们应该用父类的new方法
        return cls._instance
    # def __init__(self,name) -> None:
    #     self.name =name
    #     pass
    pass
db21 = DataBaseCls2()
print(id(db21))
db22 = DataBaseCls2()
print(id(db22))
db23 = DataBaseCls2()
print(id(db23))
# 三个地址不一样


##############################################
# 异常处理 使用try:...except:...结构
# 其余见PPT（下七）中的部分 报错类型表格等等
try: 
    print(a)  #我们故意写一个错误 a没有定义
except Exception as e: # Exception 可以捕获任何类型的异常
    print(e) 
    pass

###############################################
# 动态添加实例方法需要使用types
import types # 添加方法的库
from types import MethodType

#类
class StudentA(object):
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        pass
    def __str__(self):
        return '{}{}岁了'.format(self.name,self.age)
    pass

#对象
zyh =StudentA('张艳华',24)

def dynamicMethod(self):
    print('{}的体重是{}千克 在{}读书'.format(self.name,self.weight,self.school))
    pass

StudentA.school = '北京航空航天大学' #动态追加类属性
zyh.weight = 50  #动态追加实例对象的属性 注意这个weight只能zyh用 其他的类和对象不能用 私有

zyh.PrintInfo = types.MethodType(dynamicMethod,zyh) # 利用types方法绑定实例属性
# printInfo是为zyh新定义的方法名称，types是关键字，methodtype可能也是吧，括号里两个参数，第一个是赋给的函数（方法）名字，第二个是赋给的对象zyh
zyh.PrintInfo() #调用动态规定的方法

######################################################
# 给类绑定类方法和静态方法

#定义一个类方法用@classmethod   静态方法用@staticmethod关键字
# 类名.方法名 = xxx
@classmethod
def testClsMehod(cls):
    print('--------是一个类方法----------')
    pass


print('--------绑定类方法----------')
StudentA.addClsMethod = testClsMehod #左边是新的追加（绑定）的；类方法的名字，加在类StudentA里面了，右边值得是加的具体的内容，也就是上面写的类方法的函数
StudentA.addClsMethod() #类来调用
zyh.addClsMethod() #类对象 也可以来调用这个类方法


##静态方法的绑定：
@staticmethod
def StaMethod1(): #注意静态方法不需要参数（当然愿意设置也可以 但是需要传参）
    print('---------这是一个静态方法--------')
    pass

print('-----------绑定静态方法√----------------')
StudentA.addStaMethod = StaMethod1 #赋值绑定好
StudentA.addStaMethod() #类 调用
# zyh.addStaMethod() #类对象 也可以来调用这个类方法 但是一般不用对象来访问（之前学过），不然耗内存

#总结：动态添加方法 
# 只有实例方法的绑定需要导入types这个库
#  静态方法 和 类方法只要@关键字就行了
#再写一遍：
# 类方法的第一个参数是类对象cls，通过cls引用的类对象的属性和方法
# 实例方法的第一个参数是实例对象self，通过self引用的可能是类属性、也有可能是实例属性(这个需要具体分析)，不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
# 静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用。


############################
# slots属性
# python是动态语言，在运行的时候可以动态添加属性。如果要限制在运行的时候给类添加属性，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性。
# 只有在__slots__变量中的属性才能被添加，没有在__slots__变量中的属性会添加失败。可以防止其他人在调用类的时候胡乱添加属性或方法。__slots__属性子类不会继承，只有在当前类中有效。


#类
class StudentB(object):
    __slots__ = ('name','age','hobby') #元组的形式写要限制的属性 添加的范围 不能随便加之外的额属性
    def __str__(self):
        return '{}{}岁了'.format(self.name,self.age)
    pass

#对象
zgl =StudentB()
zgl.name = '诸葛亮'
zgl.age = 50
zgl.hobby = '运筹帷幄之中'
print(zgl)
# zgl.weight = 15 #'StudentB' object has no attribute 'weight'
# weight在slots里面没有定义属性 所以无法添加

# print(zgl.__dict__) #返回{'name': '诸葛亮', 'age': 50, 'hobby': '运筹帷幄之中'}   
##__dict__  这句话用之前需要注销掉slot那句 因为加了slot限定之后 此处的字典就不再有数据
##__dict__ 所有可以用的属性都在这储存 不足之处：占用的内存空间大


# ###### 在继承关系中使用slots：
# class subStudent(StudentB):
#     pass

# lucy = subStudent()
# lucy.name = '露西'
# lucy.gender = 'F'
# lucy.addr = '深圳'
# print(lucy.name,lucy.gender,lucy.addr) # 添加属性成功了 说明父类的slots对子类没起作用

# 需要修改成这样，就可以也对子类的属性slots起作用了：

class subStudent(StudentB):
    __slots__ = ()#关键的一句代码
    #为了可以添加其他的属性 可以在子类里面加东西：
    __slots__ = ('gender','addr')
    pass

lucy = subStudent()
lucy.name = '露西'
lucy.gender = 'F' # 报错 没有gender
lucy.addr = '深圳' # 报错 没有address
print(lucy.name,lucy.gender,lucy.addr)

###########################################################

# 实例化一个单例
class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True


a = Singleton(18, "dongGe")
b = Singleton(8, "dongGe")
print(id(a))
print(id(b))
print(a.age)
print(b.age)

a.age = 19
print(b.age)
# 2351668328992
# 2351668328992 地址一样
# 18
# 18 说明只有a属性创建成功，b和a是一样的
# 19 修改了a 发现b也变了


###########################################



















