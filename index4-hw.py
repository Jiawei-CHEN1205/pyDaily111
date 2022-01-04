###########  homework
# 写函数，接收n个数字，求这些参数数字的和
# 写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。PS:字典中的value只能是字符串或列表


# #hw-1
# def calculateN(*args):
#     result = []
#     list1= list(args)
#     for item in list1:
#         result += item
#         pass
#     return result

# forCal= tuple(input('请输入待求和参数：'))
# sum1 = calculateN(forCal)
# print(sum1)
# sum2 = 0
# for item1 in sum1:
#     sum2 +=item1
#     pass
# print(sum2)

def calcu1(*args):
    result = 0
    for item in args:
        result += item 
        pass
    return result
    pass

sumv = calcu1(1,2,3,4) #int 也就是literal[0]
print('加和结果是：{}'.format(sumv))
print(type(sumv))



# #hw-2 #### list和tuple都有下标 可以用切片
def oddList(*args):
    list1=[]
    
    index = 1
    #index指的是角标序号 而我们需要输出具体的内容，因此需要再加一个item表示具体的内容
    for item in args:
        if index%2 != 0:
            list1.append(item) #奇数位置的元素存到list1之中
            pass
        index +=1
        pass
    # print('list2={}'.format(list2[::2])) #list2相关的这几处代码也可以实现功能 步长设置为2
    return list1
    pass
rs1 = oddList(2,3,4,5,6,7,8,11,12,14,15)
print('rs1={}' .format(rs1))



#######此处的con可以是列表也可以是元组
def oddlist1(con):
    print(con[0::2])   # 0可以不写[::2]
    pass

conInput = tuple(range(24,40))
# conInput2 = list(input())
# conInput2 = tuple(input())
oddlist1(conInput)
# oddlist1(conInput2) 会把输入的每一个东西当做一个元素 包括空格 逗号 所以此方法不科学 强制转换成list/tuple也没啥用

#hw-3

###########要注意一个事情就是 截取前两位长度的时候 要求传入的数据必须是str或者是列表 否则len()函数会报错 比如int就不能判断长度

######不带key的字典输出 但是用的是list输出的：
# def detectDic(dic1):
#     list3 = []
#     for value in dic1.values():
#         if len(value)>2:
#             value11 = value[0:2]
#             list3.append(value11)
#             pass
#         else:
#             list3.append(value)
#             pass
#         pass
#     return list3
#     pass

# forDetect = {'age':'30 years old','hobby':'Soccer','height':'189cm','id':[130221,'深圳','1999','8888888']}
# detect = detectDic(forDetect)
# print(detect)



#带着key，然后value内容只截取前两个：
def detectDic(dic1):
    dictResult = {} #空字典
    for key,value in dic1.items():
        if len(value)>2:
            dictResult[key] = value[0:2] #key不变 把value赋值上去
            pass
        else:
            dictResult[key] = value #长度不超过2的 直接赋值上去
            pass
        pass
    return dictResult
    pass

forDetect = {'age':'30 years old','hobby':'Soccer','height':'189cm','id':[130221,'深圳','1999','8888888']}
detect = detectDic(forDetect)
print(detect)



