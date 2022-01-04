## 继承！子类继承父类的属性或行为，但是子类有的，父类不一定有
################单继承 一个父亲
class Creature():
    def eat(self):
        print('吃饭啦')
        pass
    def drink(self):
        print('喝水啦')
        pass
    pass
class Dog(Creature):#括号里写(creature) 表示Dog继承了这个类
    def wwj(self):
        print('小狗汪汪叫')
        pass

class Cat(Creature):
    def mmj(self):
        print('小猫喵喵叫')
        pass

dog1 = Dog()
dog1.eat() #具备了吃这个行为，是父类里面定义的
dog1.wwj() #子类中定义的行为

cat1 = Cat()
cat1.drink() #具备了吃这个行为，是父类里面定义的
cat1.mmj() #子类中定义的行为

################################
####多继承 有很多干爹
# 在小括号里有多个父类名字就是多继承

class Godd:
    def fly(self):
        print('神仙会飞')
        pass
    pass

class Money:
    def peach(self):
        print('猴子吃桃子')
        pass
    pass

class Sunwukong(Godd,Money):
    print('*'*60)
    def skill(self):
        print('七十二般变化')
        pass
    pass

swk = Sunwukong()
swk.skill()
swk.fly()
swk.peach()

################### 当父类中定义了相同的方法 执行哪个呢？
# 继承顺序的问题 深度优先：
#先找自己C的，然后找父亲一辈的，亲爹B->干爹D， 之后找爷爷的，因此干爹D＞爷爷A 前提是两个爹是一个爷爷A 否则发现输出的是A爷爷？？？
# 举个例子：
class A:
    def act(self):
        print('A的act')
        pass
    pass

class B(A):
    pass
class D(A):
    def act(self):
        print('D的act')
        pass
    pass
class C(B,D):
    pass

testC = C()
testC.act()
print(C.__mro__) #(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.A'>, <class 'object'>) 查找顺序
# mro: method resolution order 方法解析顺序

class Base(object):
    def test(self):
        print('------Base test---- ')
class Base1(object):
    def test(self):
        print('------Base1 test---------')# A继承Base
class A(Base):# 重写 test 方法
    def test(self):
        print('----A  test---------')
        # B继承Base1
class B(Base1):# 重写 test 方法
    def test(self):
        print('----B test---------')# 定义一个子类，继承自A，B
class C(A, B):
    pass
c = C()
c.test()
print(C.__mro__)  # 可以查看C类的对象搜索方法是的先后顺序，也就是继承的顺序
# ----A  test---------
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.Base'>, <class '__main__.B'>, <class '__main__.Base1'>, <class 'object'>)

#间接继承 爷爷--父亲--儿子 一般最多写三级继承
#显式的 继承父类 super().父类的内容XX，可以是__init(内容，不需要写self这个词)，也可以是父类中的方法,run,eat之类的
# super() 是自动找到父类，进而调用方法。假设继承了多个父类，那么会按照顺序逐个去找，然后再调用
class Doge(object):
    hobby = '唱歌' # 类属性
    def __init__(self,name,color) -> None:
        self.name = name 
        self.color = color
        pass
    def bark(self):
        print('小狗汪汪叫')
        pass
    pass


class KejiDog(Doge):
    def __init__(self,name,color) -> None: #重写父类的内容
        super().__init__(name,color) #表示继承父类的init属性 下面可以写其他的子类特有的东西 如身高体重
        # Doge.__init__(self,name,color) ##另一种方法表示继承父类的init属性 
        self.height = 70
        self.weight = 15
        pass
    def run(self):
        print('%s 跑的快' %self.name)
        pass
    def bark(self):
        super().bark() #表示继承父类的bark() 所以会输出两句话 一句父类的 一句下面自己的
        print('%s 小狗汪汪叫' %self.name)
        pass
    def __str__(self) -> str:
        return ('{}的颜色是{}，他的身高是{}，体重是{}'.format(self.name,self.color,self.height,self.weight))
        pass
    pass

keji = KejiDog('柯基狗','棕色')
keji.bark()
print(keji)
print(Doge.hobby) #类对象的类属性可以访问 实例属性不能直接访问（下一行） 
# print(Doge.name) #报错，实例属性只能 由 实例对象 访问
print(keji.hobby) #通过实例对象去访问类属性
# 总结：类属性可以由类对象和实例对象共同访使用；实例属性只能 由 实例对象 访问

chaiquan  = Doge('柴犬','黄色的')
#修改：
chaiquan.hobby = '喜欢大灰狼' # 通过实例对象，对类属性进行修改，可以吗？不可以！
print(chaiquan.hobby) #特定的实例对象的hobby属性被修改为 喜欢大灰狼 ，但是，下面的：
print(keji.hobby) #基本的类属性中的hobby仍然是 唱歌 也就是base类属性的部分没改

#想要修改类属性，需要从 类对象的角度去修改 而不是实例对象的角度：
Doge.hobby = '骑马赛车'
print(chaiquan.hobby) # 输出 喜欢大灰狼 因为是特定实例对象修改自己的内容
print(keji.hobby) # 输出 骑马赛车 说明 修改类属性成功

################################################################
# 类方法
# 类对象 所拥有的方法，需要用 装饰器@classmethod 来标识其为 类方法，
# 对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数，类方法可以通过类对象，实例对象调用

class People:
    country = 'China'
    # 类方法 用classmethod 来进行修饰
    @classmethod
    def get_country(cls):
        return cls.country #访问类属性
        pass
    @classmethod # 类方法 
    def change_country(cls,data):
        cls.country = data
        pass
    @staticmethod #静态方法 不带参数
    def Dataget():
        return People.country
        pass
    @staticmethod #带参数的静态方法
    def add(x,y):
        return x+y
        pass
    pass

print(People.get_country()) # 通过 类对象 来引用
p1 = People()
print(p1.get_country()) # 通过 实例对象 来引用

# python3.6之后提供的  f'{}'  方法输出：
print(f'试一试新方法：{p1.get_country()}') 
#print字符串前面加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式，如果字符串里面没有表达式，那么前面加不加f输出应该都一样.

People.change_country('英国') # 通过类对象去修改类属性country 传入data 但是如果@classmethod没有加上，就会报错，因为这样就不是类方法了，而实例方法是不能通过类对象来修改类属性的
p1.change_country('美国~') # 通过实例对象也可以去修改类属性country
print(People.get_country()) # 通过 类对象 来引用
# 类方法主要可以对类属性进行访问、修改
print('*'*60)

##########################################
# 静态方法 @staticmethod
# 类对象所拥有的方法，需要用@staticmethod来表示静态方法，
# 静态方法可以不需要任何参数 所以一般用类对象去访问
People.Dataget()
# 一般情况下，不通过实例对象去访问静态方法，耗用资源
# 为什么要使用静态方法呢？
# 由于静态方法主要用来存放逻辑性的代码，本身和类以及实例对象没有交互，
# 也就是说，在静态方法中，不会涉及到类中的方法和属性的操作
# 数据资源能够得到有效充分的利用

#返回当前系统的时间
import time # 导入第三方时间模块
class TimeTest:
    def __init__(self,hour,min,second) -> None:
        self.hour = hour
        self.min = min
        self.second = second
        pass
    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S",time.localtime())
    pass
print(TimeTest.showTime())
# 静态方法说白了就是一个独立的函数，为了封装写进类里面，类对象和实例对象都可以调用

print(People.add(10,56)) #带参数的静态方法 调用

####################
# #### 总结
# 1、类方法的第一个参数是类对象cls，通过cls引用的类对象的属性和方法
# 2、实例方法的第一个参数是实例对象self，通过self引用的可能是类属性、也有可能是实例属性(这个需要具体分析)，不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
# 3、静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用。




