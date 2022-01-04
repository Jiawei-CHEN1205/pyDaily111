

# 文件备份
def CopyFile():
    # old_file = input('请输入要备份的文件名称：')
    old_file = 'thesis1121.txt' 
    file_list = old_file.split('.') # 用.分割文件的名字 前面为名字，后面为格式，并存入列表file_list中，列表有两个元素
    new_file = file_list[0] + '_copy.' + file_list[1] #新的文件名字
    
    oldF= open(old_file,'r',encoding = "utf-8") # txt文件是gbk编码的 无法识别 所以转换成计算机认识的utf-8格式
    # oldF= open(old_file,'r')
    

    content_old = oldF.read()

    newF= open(new_file,'w')
    newF.write(content_old) #写入新文件中

    # newF.write(content_old) #写入新文件中 
    # newF.write(content_old,encoding = "ISO-8859-1", engine='python',delimiter = ";", error_bad_lines=False) #写入新文件中 

    oldF.close()
    newF.close()
    pass

CopyFile()
    
# #python3
# #以读入文件为例：
# f = open("thesis.docx","rb")#二进制格式读文件
# i = 0
# while True:
#     i += 1 
#     print(i)
#     line = f.readline()
#     if not line:
#         break
#     else:
#         try:
# #             print(line)
# #             print(line.decode('utf8'))
#             line.decode('utf8')
#             #为了暴露出错误，最好此处不print
#         except:
#             print(str(line))