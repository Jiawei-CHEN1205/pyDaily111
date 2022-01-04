################################
# ##### py内置函数

#round() 对浮点数取近似
print(round(3+2.78)) #round()可以在内部输入表达式计算，默认取整
print(round(2.65,1)) #保留一位小数



#sum(a,b) 只能两个参数 当然参数a = []是可以的 一个列表

#eval()执行字符串表达式
a,b,c = 2,3,6
print('eval执行：{}'.format(eval('a+b+c')))


#通过eval可以调用其他函数
def testEval():
    print('测试一下这个字符串')
    pass

eval('testEval()') #注意此处的格式：testEval()加了括号 然后整体加了引号，
#因为eval('......')是标准格式 带引号的 arg需要是个字符串

##############################################
## 类型转换
#str() 转为字符串
# bin() 数值转换为二进制码 hex() 16进制
print(bin(15))
print(hex(2667))

#list()将 元组 转换为 列表   tuple()反之
tup1 = () #元组()
li1 = list(tup1) # 转换
li1.append('强制转换成功')
print(li1)
advTup = tuple(li1)
print(advTup)

#### 字典操作  dict()用于创建字典
dictB = dict()
dictA = dict(name= 'cjw',age= '20y',h = 168, ppr = [88,99,00])
#注意一个问题，在用dict()函数创建字典的时候，关键字key的部分，不能带引号
#而之前学的另一种普通的创建方式，是这样的：
# dictM = {'pro':'艺术','school':'北影'} 这种直接用大括号里面冒号键值对的形式，是需要写单引号的
dictB['name'] = '李易峰'
dictB['age'] = '30'
dictB['pos'] = '歌手'
print(dictB)
print(dictA)


##########################
#序列操作函数 —— str 元组 list
# all()  可迭代参数里的内容 是否都是TRUE 、有空或0或false 为false
print(all(())) #返回True 有个元组 虽然元组为空 但是有元素=空元组 所以不是none 所以返回TRUE
print(all([])) #True
print(all([''])) #False
print(all((1,2,0))) #False
print(all([13,2,False])) #False
# any() 至少有一个非空/0/false 就返回TRUE 类似于or
print(any([0,1])) #true


########## sorted()
# # 函数 对所有可迭代对象进行排序操作
# sort 和 sorted 的区别：
# 1、sort应用在list上， 而sorted可以对所有的可迭代对象；

li2 = [2,45,1,67,23,10] #原始对象；
li2.sort() #list的排序方法 直接修改原始对象 后缀形式使用.sort()函数
print(li2) #[1, 2, 10, 23, 45, 67]

af_List2 = sorted(li2) #使用sorted() 函数 默认是升序
print(af_List2)
#现在来一个降序排序的：
af_List2 = sorted(li2,reverse = True) #上面的升序本质是reverse = False
print(af_List2)


# sorted()应用于元组
tupAA = (2,999,7.8,90,11)
st_tupAA = sorted(tupAA) #st_tupAA = sorted(tupAA,reverse =True)
print(st_tupAA)

#reverse() 反转函数 该函数没有返回值 但是会对原来的列表反向排序 所以输出原始list才能看到效果
ad_list2 = li2.reverse()
print(ad_list2) #返回值是none 
print(li2) #返回值是[67, 45, 23, 10, 2, 1]

######## zip() 用来打包列表，返回元组列表
s1 = ['a','b','c','d']
s2 = ['你','我','他','她']
s3 = [95,99,93]
print(zip(s1,s2)) # <zip object at 0x000001AB0EF4AC48>
# 可以用列表的形式展示我们的打包后的结果，相当于组队了：
print(list(zip(s1,s2))) 
# [('a', '你'), ('b', '我'), ('c', '他'), ('d', '她')]
# 都是以元组的形式返回的 两个对象的相同索引位置的元素打包在一起
# 个数以最小的那组为准 例如s3只有三个元素 则按照少的 也就是三个 来压缩:
print(list(zip(s2,s3)))  #[('你', 95), ('我', 99), ('他', 93)]


######zip()例子
# def printBookInfo():
#     books = [] #存储所有图书的信息 list
    
#     idBook = input('请输入编号：每个项以空格分隔') #str
#     bookname = input('请输入书名：每个项以空格分隔') #str
#     posBook = input('请输入书的位置：每个项以空格分隔') #str
    
#     idList = idBook.split(' ')
#     nameList = bookname.split(' ')
#     posList = posBook.split(' ')
    
#     bookInfo = zip(idList,nameList,posList) # zip处理 注意打包的对象是加了split之后的那一组
    
#     for bookItem in bookInfo:
#         '''遍历图书信息进行存储'''
#         dictInfo = {'编号':bookItem[0],'书名':bookItem[1],'位置':bookItem[2]}
#         books.append(dictInfo) #将字典对象添加到list容器中
#         pass

#     for item in books: #打印打包好的信息
#         print(item)
    
# #调用一下！
# printBookInfo()
# 请输入编号：每个项以空格分隔1 2 3
# 请输入书名：每个项以空格分隔Python c++ matlab     
# 请输入书的位置：每个项以空格分隔A1 B13 C8
# {'编号': '1', '书名': 'Python', '位置': 'A1'}
# {'编号': '2', '书名': 'c++', '位置': 'B13'}
# {'编号': '3', '书名': 'matlab', '位置': 'C8'}

##########################
## enumerate()函数
# 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
# 一般用在 for 循环当中
seasons =  ['spring','summer','fall','winter']
for index,item in enumerate(seasons):
# for index,item in enumerate(seasons,5): #更改起始位置下标0-->5
    print(index,item)
    # print(item)
    pass
#第一行效果：
# 0 spring
# 1 summer
# 2 fall
# 3 winter
#第二行效果：
# spring
# summer
# fall
# winter

#或者按列表呈现：
aaa = list(enumerate(seasons))
print(aaa)  #[(0, 'spring'), (1, 'summer'), (2, 'fall'), (3, 'winter')]
#更改起始位置(下标默认从0开始)：
aaa2 = aaa = list(enumerate(seasons,start=7))
print(aaa)  #[(7, 'spring'), (8, 'summer'), (9, 'fall'), (10, 'winter')]

# 字典里应用enumerate()
dictEnu = {}
dictEnu['上午'] = 'Rp写作'
dictEnu['中午'] = '外卖'
dictEnu['晚上'] = '学习机器学习'
# print(dictEnu)
for item in enumerate(dictEnu):
    print(item) #打印的都是key
# (0, '上午')
# (1, '中午')
# (2, '晚上')
for index,item in enumerate(dictEnu):
    print(item) #打印的都是key
# 上午
# 中午
# 晚上
for index,item in enumerate(dictEnu.values()):
    print(index,item) #打印的都是value 因为是.values() 第一个index参数是下标
# 0 Rp写作
# 1 外卖
# 2 学习机器学习
for index,item in enumerate(dictEnu.values()):
    print(item) #打印的都是value
# Rp写作
# 外卖
# 学习机器学习
for index,item in enumerate(dictEnu.items()):
    print(item) #打印的是key,value组合 因为是.items()
    #此处item充当了key+value的位置 index仍然为下标
# ('上午', 'Rp写作')
# ('中午', '外卖')
# ('晚上', '学习机器学习')
for index,item in enumerate(dictEnu.items()):
    print(index,item) #打印的是key,value组合 因为是.items()
# 0 ('上午', 'Rp写作')
# 1 ('中午', '外卖')
# 2 ('晚上', '学习机器学习')

######################################################
# set '集合' 无序 不重复的容器 类似字典 但是 只有key 没有value 
# 常见操作 add() clear() etc.
# 创建集合 用{}
#创建空集 setA = set()
set1 = {1,2,3,4}
print(type(set1)) # <class 'set'>
set1.add('py')
print(set1) # {1, 2, 3, 4, 'py'}

# set1.clear() # 清空
# print(set1) # 空集set()
 
#差集difference() 或者 集合a-b
set2 = {99,-2,'bala',78,-13,7,'福尔摩斯探案集',100}
set3 = {13,23,99,19}

diff = set2.difference(set3)
print(diff)
#相当于：
print(set2 - set3) #也是差集的意思

#交集 intersection() 或者符号 &
print(set2.intersection(set3))
print(set2 & set3)

# 并集 union() 或者 符号|
print(set2.union(set3))
print(set2 | set3)

#pop()移除集合中数据 并且同时删除
# pop 数据从小到大排序,移除非负最小值（栈元素），如果有字符，则随机排序后删除第一项，所以运行结果每次可以不一样
# set2.pop()
# print(set2)

#删除指定数据discard()
set2.discard(78) #删掉了78这个元素
print(set2)

# 更新集合 update 两个集合
set2.update(set1)
print(set2)
#{1, 2, 99, '福尔摩斯探案集', 100, 'bala', 7, 3, 4, -13, 'py', -2}
#set2变成了和set1取并集之后的样子
print(set1)













