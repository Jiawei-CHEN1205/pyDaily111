from os import name


print('Hello python')
print('学习--机器学习哈哈哈')
print('人生苦短，我用Python')
#print('人生苦短，我用Python')
# 注释信息 Ctrl+/ 单行注释
a=10
print(a)
b='吴老师'
print(b)
c=True
print(c)
print(type(a))
print(type(b))
print(type(c))

#元组类型tuple
z=()
print(type(z))
#列表类型list
c=[]
print(type(c))
#字典类型
d={}
print(type(d))

a=7
b=3
print(a+b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)


c,d = 10,7
print(c==d)
print(c!=d)
print(c>d)
print(c<d)
print(c>=d)
print(c<=d)

a,b,c,d = 23,18,10,3
print(a+b>c and c<d)#false
print(c>d and a>b)#true
print(not a>b)

#a += c #表示 a= a+c
#print(a)
a **= 2 #表示 a的平方
print(a)


# name='小米'
# classPro='清华附中3班'
# agePro= 19
# print('我的名字是%s，来自【%s】今年%d岁'%(name,classPro,agePro))
# print('我可以\n换行吗')#\n换行 但是print自带换行功能

# qq='1053818040'
# print('我的qq是：%s' %qq) 
# #注意中间 不用逗号 隔开引号内的内容和后面的%qq


# #另一种格式化输出的方法   .format()
# print('姓名：{}'.format(name))
# print('qq：{}'.format(qq))
# print('----------format--------')
# #两个以上的话
# print('姓名：{}，qq：{}'.format(name,qq))


#input 练习
name=input("请输入您的姓名：")# 输入用的是 双引号！
qq=int(input("请输入您的qq：")) #强制转换int()
addr=input("请输入您的地址：")
phone=input("请输入您的电话：")

# print('姓名：{}'.format(name))
# print('qq：{}'.format(qq))
print('姓名：%s, qq号：%d' %(name,qq))
print('addr：{}'.format(addr))
print('电话：{}'.format(phone))



