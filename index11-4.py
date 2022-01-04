# 文件定位，指的是当前文件指针读取到的位置，光标位置。在读写文件的过程中，如果想知道当前的位置，可以使用tell()来获取
# 注意：utf-8格式的中文每个字占位3字节，gbk是2字节



# with open('thesis1121.txt','r',encoding='utf-8') as f:
#     print(f.read(4))
#     print(f.tell()) # 输出结果 12 因为4*3 = 12
#     print(f.read(2))
#     print(f.tell()) # 输出结果 18 因为6*3 = 18
#     pass

######## truncate 可以对源文件进行截取操作
# fObj = open('thesis1121.txt','r',encoding='utf-8')
# print(fObj.read())
# fObj.close()
# print('截取之后的数据......')

# fObj2 = open('thesis1121.txt','r+',encoding='utf-8') #注意需要可写入的模式才能用truncate
# fObj2.truncate(21) # 只截取留下21个字符的内容 其余的舍去了
# print(fObj2.read())
# fObj2.close()

# 如果在操作文件的过程，需要定位到其他位置进行操作，用seek()
# seek(offset, from)有2个参数,offset，偏移量单位字节，负数是往回偏移，正数是往前偏移，from位置：0表示文件开头，1表示当前位置，2表示文件末尾

with open('thesis1121.txt','rb') as ff: #二进制格式读取
    # 注意：r模式数字代表字符数，rb模式数字代表字节数 字符数乘上对应的编码占位才是=字节数
    data = ff.read(3) #3个小写的英文字符，3个字节，不是3个字符
    print(data) # b'\xe6\x9c\xba'
    print(data.decode('utf-8')) #解码

    ff.seek(-3,1) #当前位置（1），往回（负号）3个字节，相当光标回到了文档的开头
    print(ff.read(12).decode('utf-8')) #从头读取12字节

    ff.seek(-15,2) #光标从文档末尾 回退15个字节
    print(ff.read(3).decode('utf-8')) #读出倒数第五个字
    # 注意一个\n占两个字节 注意一下换行符的事情
    pass

















