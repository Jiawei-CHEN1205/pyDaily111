############### 多态 
# 顾名思义就是多种状态、形态，就是同一种行为 对于不同的子类【对象】有不同的行为表现
# 要想实现多态 必须的有两个前提需要遵守：
# 1、继承：多态必须发生在父类和子类之间
# 2、重写: 子类重写父类的方法

# 多态有什么用:
# 增加程序的灵活性
# 增加程序的拓展性

#大类 animal
class Animal():
    def say_who(self):
        print('我是一个动物......')
        pass
    pass

class Duck(Animal):
    def say_who(self): # 重写 体现多态
        print('我是一只鸭子......')
        # return super().say_who()
        pass
    pass

class Elephant(Animal):
    def say_who(self): # 重写 体现多态
        print('我是一只大象......')
        pass
    pass

class Fish(Animal):
    def say_who(self): # 重写 体现多态
        print('我是一条鱼......')
        print(15)
        pass
    pass
# 另一个大类
class Human:
    def say_who(self): # 重写 体现多态
        print('我是人类......')
        pass
    pass
class Xming(Human):
    pass

def comInvoke(obj): #统一去调用
    '''
    obj: 对象的实例
        '''
    obj.say_who()

listObj = [Duck(),Elephant(),Fish(),Xming()]
for item in listObj:
    '''
    用for循环依次获取定义在列表中的类（class），
    再将值传给函数comInvoke（obj），对say_who进行调用
    '''
    comInvoke(item)

# 不关注obj是什么类型，也不关心是不是来自于同一个父亲Animal/Human, 
# 只要它obj具备了say_who() 这个函数，就可以调用

#########鸭子类型(duck typing)
# 在程序设计中，鸭子类型（英语：duck typing）是动态类型的一种风格。在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定。
#  “鸭子测试”可以这样表述：
# “当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。”
# 在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的。
# Python 天生就是支持多态，因为他是弱类型语言，不需要指定类型









