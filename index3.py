#######高级数据类型

# #字符串
# #print(type(Name...))
# # e.g.
# Test = 'Chenjiawei'   #索引从0开始 第一个字符是[0]
# print(Test[0])
# print('获取第一个字符%s' %Test[0])
# print(Test[1])
# print(Test[7])


# #字符串的几个函数
# name = '  pEterHum   '
# name1 = 'chenjiawei'
# print(name1.capitalize()) #首字母大写
# print(name.strip())   #去除字符串中两侧的空格  lstrip 是左侧空格移除 rstrip 是右侧空格

# a=name.swapcase()  #大小写全转换
# print(a)


# #XXXX的内存地址 id(XXXX)

# c=name1  #复制c 只是把name1地址给了c
# print('name1的内存地址为%d' %id(name1))
# print('c的内存地址为%d' %id(c))
# #发现结果是一样的




# #查找目标数据 在序列中的位置 find()函数
# dataStr = 'I Love Python'
# print(dataStr.find('P'))  #输出的是数字 第几个位置（包括空格也有占位）
# print(dataStr.find(' '))  #只能找到第一处的空格位置
# print(dataStr.find('k')) 
# #注意第一个位置是0  找不到则返回-1

# #index()函数也能查找 但是找不到的话index会报错而find 不会
# print(dataStr.index('P'))
# # print(dataStr.index('k'))

# #判断以什么来开头和结尾 startswith() endswith() 返回bool类型
# print(dataStr.startswith('m')) #返回 false
# print(name.endswith(' ')) #返回true


# print('abc123'.isdigit())  #检查是否是 数字  此返回false

# #其他函数见PPT


# ###################################
# strMsg = 'hello world of python!'
# #切片功能   slice  [start:end:step]
# #左含 右不含
# print(strMsg)  #全部 
# print(strMsg[4]) #第五个 [0]开始
# print(strMsg[2:5]) #3-5 不含第六[5]个
# print(strMsg[2:]) #第三个到最后
# print(strMsg[:9]) #一开始到第9[8]个


# ############# 列表 list ##################  [] 创建 逗号分割
# # li = []   #定义了一个 空列表
# li = [1,2,3,"你好"]
# print(len(li))  #列表长度 4
# print(len(name))  #字符串的长度也可以这样输出
# print(type(li))

# #查找
# listA = ['abcd',785, 12.23,'求职',True] #注意12.23前面的一个空格不包括不影响
# print(listA)
# print(listA[1:3]) #输出两个 [1]and[2] 即[785, 12.23]
# print(listA[1:])
# print(listA[:3])
# print(listA[::-1]) #负数的步长 表示数据从右向左输出
# print(listA*3) #copy 3次
# print('---------增加----------')
# listA.append(['fff','dddd'])
# print(listA)
# #输出效果 嵌套了一个小列表在最后：
# #['abcd', 785, 12.23, '求职', True, ['fff', 'dddd']]
# #继续加
# listA.append(88888) 
# print(listA)
# #['abcd', 785, 12.23, '求职', True, ['fff', 'dddd'], 88888]

# #在特定位置插入数据insert(数字位置,'内容')
# listA.insert(2,'帅气boy')  #[2]位置插入内容 2是索引
# print(listA)
# #['abcd', 785,'帅气boy', 12.23, '求职', True, ['fff', 'dddd'], 88888]

# rsData = list(range(10)) #强制转换成list对象 而且是十个数的 即0-9十个数字构成的列表
# print(type(rsData))
# print(rsData)
# # listA.extend(rsData)  #扩展extend() 相当于批量增加 把整个0-9加到listA后面
# #你也可以这么增加一堆内容：
# listA.extend([11,22,33,44]) 
# print(listA)

# print('---------修改----------') 
# print('修改之前，',listA)
# listA[8] = 'peterM'  #想改哪个，直接对应数字处 = '改后内容'
# listA[5] = 99832
# print('修改之后，',listA)

# print('---------删除 del----------')
# listB = list(range(10,31))
# print(listB)

# del listB[8]
# print(listB)

# del listB[2:5] #批量删除 加切片slice[2:5]
# print(listB)

# #移除指定元素（具体的数据内容） remove
# listB.remove(28) #而且只能移除找到的第一个元素
# print(listB)
# #pop 移除指定的项（指索引序号） // 弹出 堆栈操作
# listB.pop() #pop()不加  默认移除的是最后一个数据
# print(listB)

# listB.pop(3)
# print(listB)

# #index() 返回这个内容的序号位置
# m=listB.index(24) #可以带查找范围限制
# print(m)  #返回 9

# print(listB.index(21,3,7))  #[3]--[6]的位置内查找 返回值6




# ############ 元组  ################# () 创建 逗号分割 是不可变的 只具有获取查询功能 而无修改功能
# tupleA = ()  #空元组
# tupleA = ('abdcg',89,0.932,'tom',[11,22,33])
# #查询
# for item in tupleA:
#     print(item, end=' ')
# #取特定内容
# print(tupleA[2:4]) #(0.932, 'tom')

# print(tupleA[-2:-1:]) #('tom',) 倒着取下标为-2到-1区间的
# print(tupleA[-4:-2:]) #(89,0.932) 倒着取下标为-2到-1区间的 但是显示的时候是原来的正序

# print(tupleA[4:2:-1]) #([11, 22, 33], 'tom') 倒着取 显示的也是倒过来的  含右不含左
# print(tupleA[::-1]) #([11, 22, 33], 'tom', 0.932, 89, 'abdcg')
# print(tupleA[::-2]) #两个(隔一个)取一个 而且是反转的  -3同理

# #元组中的列表list可以修改 字符串之类的不可以
# #举例
# # tupleA[0]是个字符串
# #tupleA[0] = 'ccccc' 是错误的

# # print(id(tupleA))
# print(id(tupleA[4])) #原地址
# tupleA[4][1] = 9988888 # tupleA[4]是个列表 tupleA[4][1]指的是列表的第二个元素
# print(tupleA)  #修改成功！[11, 9988888, 33] 内容变了，但是该列表的地址不变
# print(id(tupleA[4])) #现地址 不变的

# # 当元组中只有一个元素时，要加上逗号，不然后解释器会当做其他类型来处理
# #强制转换成tuple
# tupleC = tuple(range(10))
# print(tupleC.count(8))
# print(tupleC)


# tupleD = range(10),8    #也是元组 但是第一个元素是一个range 第二个元素是8
# print(type(tupleD))
# # print(tupleD)
# print(len(tupleD)) #长度只有2
# print(tupleD.count(8))  #因此只有一个8（第二个元素）。第一个元素是个整体，所以不能找到更里面一层的“8”数字

################### 字 典 ####################

dictA = {} #创建空字典
# [key] = value 赋值添加数据
dictA['name'] = '李易峰'
dictA['age'] = 30
dictA['pos'] = '歌手'
print(dictA)

#也可以在定义的时候就添加好内容：
dictB = {'pro':'艺术','school':'北影'}
dictB['name'] = '李易峰'
dictB['age'] = '30'
dictB['pos'] = '歌手'
print(dictB)
print(len(dictB))
#{'pro': '艺术', 'school': '北影', 'name': '李易峰', 'age': 30, 'pos': '歌手'}
#长度为5

#查找#
print(dictA['name']) #通过键获取对应的值
#修改对应值
dictA['name'] = '谢霆锋'
dictA.update({'age':'35'}) #update()也是一种修改的函数，也可添加信息
dictA.update({'height':1.80})
print(dictA)

#获取所有的键
print(dictB.keys())
#获取所有的值
print(dictB.values())
#获取所有的项（键值对）
print(dictB.items())
#遍历
for key,value in dictA.items():
    print('%s=%s' %(key,value))
    pass



####删除 del
# del dictA['age'] #两种指定键删除的方法
dictA.pop('age')
print(dictA)

########### 排序 
# # 1--按照key排序
print(sorted(dictB.items(),key = lambda d:d[0]))
# # 2--按照value排序
print(sorted(dictB.items(),key = lambda d:d[1]))
#注意一个事情，按照value排序的时候，字典里面的value，每一项的格式要统一，因此去把age的数字改成了str类型

#########合并等操作######

#共有方法  + * in
strA = '人生苦短'
strB = '我用Python'


listA = list(range(10))
listB = list(range(10,20))

tupleA = ('just',' be', ' yourself')
tupleB = ('ooooooohooray!',)

#合并# 用+号操作的 #神奇的是，字典不能用+号合并
print(listA + listB)  
print(strA +' '+ strB)
print(tupleA +tupleB)

#复制 *号
print(strB*2)
print(listA*3)
print(tupleB*2)


#in 判断对象是否存在 返回bool类型
print('我' in strA) #False
print(9 in listA) #True

dictA = {'name':'peter'}
print('name' in dictA) #True











