##################### Lesson 2 ############

# score = int(input('请输入您的成绩：'))
# #注意输入默认是str类型

#单分支 if
# if score<=60:  #注意加冒号 然后 满足就输出下面的语句
#     print("Come on!")
#     pass #空语句 可以不写 下一句顶格就行

# print("语句运行结束")

#双分支
# if score<=60:  #true
#     print("Come on!")
#     pass #空语句
# else:       #false
#     print('good!')
#     pass


# #多分支
# if score>=90:
#     print('GPA=4.0')
#     pass
# elif score>=85:  #elif 也需要冒号
#     print('GPA=3.7')
#     pass
# elif score>=80:
#     print('GPA=3.5')
#     pass
# else:  #else 可以没有
#     print('OMG!下次加油！')

# print("语句运行结束")

################################
#猜拳机 #计算机和人的输入
# count = 1
# import random #随机数 导入
# #石头0 剪刀1 布2
# while count<=10:
#     person = int(input('请出拳：[石头0 剪刀1 布2]'))
#     computer=random.randint(0,2)#规定随机数的范围 整型int 而且从0-2
#     if person<=2 and person>=0:
#         if person==0 and computer==1:
#             print('you win!')
#         elif person==1 and computer==2:
#             print('you win!')
#         elif person==2 and computer==0:
#             print('you win!')
#         elif person==computer:
#             print('50 to 50')
#             print('computer=%d' %computer)
#         else:
#             print("sorry,you lose~")
#             print('computer=%d' %computer)
#         count+=1  #注意看清count++的位置
#     else:
#         print('please choose again!')
#         count+=1  #如果在这里也加上count++ 就表示总共次数是十次，不加的话就是有效次数是十次
#     print("剩余次数%d" %(11-count))
#     pass
# print("语句运行结束")





##########################
#循环 while
#1、有初始值
#2、有条件表达式
#3、变量[循环体内计数变量]的自增自减，否则会造成死循环
#使用条件：循环的次数不确定，是依靠循环条件来判断的

#e.g.输出1-100
# index = 1
# while index<=100:
#     print(index)
#     index+=1
#     pass
# print('finish')

################### 99乘法表 ############
# row=1
# while row<=9:
#     column=1
#     while column<=row:
#         print('%d*%d=%d' %(row,column,row*column),end=" ")#加上end=" "相当于是把print函数里面默认的换行符改成了空格，不让他换行 可以呈现三角的九九乘法表
#         column+=1    
#         pass
#     row+=1
#     print('\n') #或者print()
#     pass


# row=9  #倒三角的乘法表
# while row>=1:
#     column=1
#     while column<=row:
#         print('%d*%d=%d' %(row,column,row*column),end=" ")#加上end=" "相当于是把print函数里面默认的换行符改成了空格，不让他换行 可以呈现三角的九九乘法表
#         column+=1    
#         pass
#     row-=1
#     print('\n') #或者print()
#     pass


############等腰三角形########
# row=1
# while row<=8:
#     space=1
#     while space<=8-row:
#         print(' ',end=' ')
#         space+=1
#         pass
#     star=1
#     while star<=2*row-1:
#         print('*',end=' ')
#         star+=1
#         pass
#     print()
#     row+=1
#     pass



########## for循环############# 字符串 列表 均可以遍历
#遍历操作，依次提取容器内的每个值
# for 临时变量 in 容器：
#     执行代码
# tags='我是一个中国人' #字符串本身就是一个字符类型的集合
# for item in tags:
#     print(item,end='')
#     pass

#range 此函数可以生成一个数据集合列表 (起始:结束:步长) 左包含 右不包含 步长不能为0，默认为1  注意和MATLAB区分
# for data in range(1,101):
#     print(data,end=' ')
#     pass

#求累加和 1-100
# sum=0
# for data in range(1,101):
#     sum += data
#     pass
# print('sum=%d' %sum)


# for data in range(50,201):
#     if data%3==0:
#         print(data)
#         pass
#     else:
#         print('%d不能被3整除' %data)
#         pass
#     pass

######## break 和 continue
#break  代表中断结束 满足条件直接结束本层循环
#continue 结束本次循环 但继续进行下次循环(当continue 的条件满足时，本次循环剩下的语句将不被执行，后面的循环继续)
#这两个关键字只能用在循环



#累加和不超过100的最大的sum
# sum=0
# for item in range(1,51):
#     if sum>100:
#         print('item=%d' %(sitem-1))
#         break #退出循环体
#     sum+=item
# print('sum=%d' %(sum-item))
# # print('sum=%d' %sum)



#continue的使用
# for item in range(1,100): #只打印奇数，所以偶数的话就continue不打印
#     if item%2 == 0:
#         continue
#         # print('no act')#这句话是不会输出的 因为到上一行的continue就跳出这一层循环了 难怪IDE显示是灰色的
#         pass #灰色 不用写这句
#     print(item,end=' ')
#     pass


# relly = 'I LOVE Detective Conan'
# for data in relly:
#     if data == 'e' or data == 'E':
#         continue
#     else:
#         print(data,end='')
#     pass

# relly = 'I LOVE Detective Conan'
# for data in relly:
#     if data == 'e':
#         break
#     else:
#         print(data,end='')
#     pass


###### for的嵌套实现九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d' %(j,i,i*j),end=' ')
#         # j+=1 不需要变量++因为遍历数组就是在++了
#         pass
#     # i+=1 不需要变量++因为遍历数组就是在++了
#     print() #控制换行
#     pass

######  for和else 的配合使用
# key = 'ccl306501'
# for i in range(3):  ####这个range(3)里面的3 指的是3次  (0,2,1)
#     key1=input('请输入账号密码：')
#     if key1 == key:
#         print('密码正确，登陆成功...')
#         break ####退出循环 else不会执行
#         pass
#     else:
#         print('密码错误，请重新输入')
#         pass
#     # print(i)
#     pass
# else:
#     print('密码错误超过三次，账户被锁定')


######  while和else 的配合使用 差不多

###### day 2 作业 ######

### 2.1 猜年龄
import random
age = random.randint(17,28)

flag = 1
while flag == 1:
    for count in range(3):
        guess = int(input('请输入您猜测的年龄(17~28):'))
        if guess == age:
            print('恭喜你猜对了')
            print('正确答案是：%d' %age)
            break
        else:
            print('sorry,请继续猜一下')
            pass
        pass
    else:
        print('猜错三次，请问是否继续游戏？(y/n)',end=' ')
        decision = input('')
        if decision == 'y' or decision == 'Y':
            continue  #####直接回跳到while那一句 然后从 for count...开始
        #注意continue跳出的是“循环”，而 if之类的只是条件语句而非循环，因此，此句跳出的是大的for//else循环体，因此直接到了while那一句
            pass
        elif decision == 'n' or decision == 'N':
            print('正确答案是：%d' %age)
            pass #####继续走出此次循环 下一句就是“游戏结束啦”
        else:
            print('输入的语法格式有误，默认退出游戏')
            pass
        pass
    print('游戏结束啦！')
    flag = 0
    pass



        







