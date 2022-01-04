######################## 模块 Modeltest
__all__= ['HappyBirthday','differ']

# __all__ 作用是：限制外部可以调用的本模块里面的内容,搭配from Modeltest import * 这种调用方法使用，
# 其余的 类似import XX 这种全部导入的 不会受到all的限制




def HappyBirthday(name):
    # print('祝%s小帅哥生日快乐！！！' %name)
    print('祝{}小帅哥生日快乐！！！' .format(name))
    pass



def differ(a,b):
    return a-b
    
def printInfo():
    return '这个是没有被包括在__all__里面的函数'

if __name__ == '__main__':
    HappyBirthday('cjw')

    print('模块__name__变量是：{}' .format(__name__))
    # 模块__name__变量是：__main__  说明名字是main 
    # 而在调用的文件index11-7中，name的名字是Modeltest

    pass























