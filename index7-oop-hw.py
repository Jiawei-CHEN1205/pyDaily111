# 1、编写一段代码以完成下面的要求
# 定义一个Person类,类中要有初始化方法,方法中要有人的姓名,年龄两个私有属性.
# 提供获取用户信息的函数.
# 提供获取私有属性的方法.
# 提供可以设置私有属性的方法.
# 设置年龄的范围在(0-120)的方法，如果不在这个范围，不能设置成功.


class LenAgeExcept(Exception):
    def __str__(self):
        return '[error:] 你输入的年龄超过了0-120的范围，请输入正确的年龄'


class Person(object):
    def __init__(self,name,age) -> None:
        self.__name = name
        self.__age = age
        pass
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name = name
        pass
    def set_age(self):
        try:
            age = int(input('请输入年龄：'))
            if age <= 0 or age >= 120:
                raise LenAgeExcept()
            pass
        except LenAgeExcept as err:
            print(err)
        else:
            self.__age = age
            # print('没有异常')
        pass

    def __str__(self):
        return '{}的年龄是{}岁'.format(self.__name,self.__age)
    def __call__(self, *args, **kwds): # __str__ 实例为属性的时候调用    __call__实例为函数的时候调用
        # return self.__name+'的年龄啊啊啊是：'+self.__age
        print(self.__name+'的年龄啊啊啊是：'+str(self.__age))  #注意只能输出str格式print如果连一起输出，所以把年龄强制转换成str了
    name = property(get_name,set_name)
    age = property(get_age,set_age)


# try:
#     age = int(input('请输入年龄：'))
#     if age <= 0 or age >= 120:
#         raise LenAgeExcept()
#     pass
# except LenAgeExcept as err:
#     print(err)
# else:
#     print('没有异常')
#     pass

kid = Person('怪盗基德',17)
kid()  #__call__函数结合 将实例对象以函数的形式去调用
print(kid)
kid.set_age()
print(kid)
kid.name = '工藤新一'
print(kid)
kid() #__call__函数结合 将实例对象以函数的形式去调用




# 2、请写一个单例模式
class SingleMode(object):
    __instance = None
    __firstInit = False

    def __new__(cls,age,name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,age,name):
        if not self.__firstInit:
            self.age = age
            self.name = name
            SingleMode.__firstInit = True
        
am = SingleMode(17,'铃木园子')
bm = SingleMode(18,'京极真')

print(id(am))
print(id(bm))
print(am.age,am.name)
print(bm.age,bm.name)

am.age = 21
print(am.age,bm.age)
# 2467211883912
# 2467211883912
# 17 铃木园子
# 17 铃木园子
# 21 21


# 3、创建一个类，并定义两个私有化属性，提供一个获取属性的方法，和设置属性的方法。利用property 属性给调用者提供属性方式的调用获取和设置私有属性方法的方式。

# 省略


# 4、创建一个Animal类，实例化一个cat对象，请给cat对象动态绑定一个run方法,
# 给类绑定一个类属性colour,给类绑定一个类方法打印字符串'ok'。

class Animal(object):
    @classmethod
    def INfo(cls):
        print('ok') #给类绑定一个类方法打印字符串'ok'
        pass
    
# 给类绑定一个类属性colour （指的是动态绑定）
Animal.color = '蓝色'

cat = Animal()

import types #为了动态绑定一个实例方法给cat 导入types库
def run(self):
    print('小马快跑')
    pass

cat.run1 = types.MethodType(run,cat) #给cat对象动态绑定一个run方法 run1是为了区分，实际上使用的时候一般写同名的
cat.run1() #调用实例方法

print(cat.color,Animal.color)
Animal.INfo()





























































