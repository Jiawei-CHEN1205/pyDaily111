###########day11 文件读写

# 打开文件 open
# 默认的是gbk编码，这个是中文编码，
# 更好的方式是打开一个文件的时候给它制定一个编码类型



encode = 'utf-8'

# open('C:/A--HITsz_files/4--learnPY/words.txt','r+')
# fobj = open('test1121.txt','w') #当前路径
# # open('./test1121—1.txt','w') #也是当前路径
# # fobj.write('苍茫的天涯是我的爱\n')
# fobj.write('狂风卷积着乌云\n') # w操作 每次会覆盖之前的内容
# fobj.close() #保存＋关闭文件

# # 以二进制的形式去写数据
fobj = open('test1121.txt','wb') #str-->bytes
fobj.write('啊啊啊啊狂风卷积着乌云bbb\n'.encode('utf-8')) # .encode规定了输入的内容是utf-8，不然会报错（str和二进制不同） 
fobj.close() #保存＋关闭文件

# a用于追加 必须是str
# fobj = open('test1121.txt','a')
# # fobj.write('山雨欲来风满楼')
# # fobj.close()
# fobj.write('山雨欲来风满楼\n')
# fobj.write('树欲静而风不止\n')

# ab 二进制形式追加
fobj = open('test1121.txt','ab')
fobj.write('啊啊啊啊山雨欲来风满楼\n'.encode('utf-8'))
fobj.write('啊啊啊啊树欲静而风不止\n'.encode('utf-8'))
fobj.close()
#注意前后编码方式的一致性 防止出现乱码 例如几次都是wb ab 格式再统一为utf-8就不会乱码 否则str和二进制读写混用会导致一部分乱码


# rb 二进制格式 读取文件数据
f = open('test1121.txt','rb')
data =f.read() 
# print(data) #发现print(data) 完全是二进制代码
print(data.decode('utf-8')) # 可以用decode解码 前面规定了utf-8 此处就用此解码 后面的操作里面是字符gbk格式的编码 那么解码的时候就是用gbk
f.close()

####################重新整理并写一次文件
fobj = open('test1121.txt','w') #当前路径
fobj.write('狂风卷积着乌云\n') # w操作 每次会覆盖之前的内容
fobj.close() #保存＋关闭文件

fobj = open('test1121.txt','a')
fobj.write('山雨欲来风满楼\n')
fobj.write('树欲静而风不止\n')
fobj.close() #保存＋关闭文件

# read读取文件数据
f = open('test1121.txt','r') #r 读取的是gbk格式
content = f.read(4) #只读4个字符 第二次读取的位置 从第一次读取之后继续读取
print(content)

# print(f.read()) #全部读取.read()无参数 在这里由于已经读了4个，因此是把剩余的都读出来了

#readline() 读取一行
print(f.readline())

#readlines() 读取全部的内容 但是是按行读取的 返回的是一个list，可以用数字规定读取范围（见下方注释）
print(f.readlines(7)) # 山雨欲来风满楼是七个字 这里写7或更小 就是只有这一行 写8或更大就会读出两行字
# 注意，这里老师讲错了，不是指定的第一行第二行，而是读取的字符长度
# 假如指定长度小于第一行，则返回第一行全部内容
# 指定长度多于第一行，但少于第二行结尾，则返回前两行，以此类推

f.close()

# rb 二进制格式 读取文件数据
f = open('test1121.txt','rb')
data =f.read() 
# print(data) #发现print(data) 完全是二进制代码
print(data.decode('gbk')) # 可以用decode解码
f.close()  ###一定要关闭文件！不然不能后续操作


# with 上下文管理对象 自动释放
# with 语句，不管在处理文件过程中是否发生异常，都能保证 with 语句执行完毕后已经关闭打开的文件句柄。
def main():
    with open('test1121.txt','r') as fl:
        print(fl.read(13)) #不需要手动加close函数了
        pass
    pass
main()

with open('test1121.txt','a') as fl:
    fl.write('今天和电脑拆机过不去了哈哈哈哈哈\n') #追加成功
    pass

# SyntaxError时候，第一行写：# -*- coding: gbk -*-


################################################

    
    
    
    
    














