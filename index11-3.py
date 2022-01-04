#如果处理超大文件，一次将全部内容读取出来显然是不合适的，在需求1（文件index11-2）的基础上改进下代码，让它备份大文件也不会导致内存被占满。

def CopyFile():
    # Old_File = input('请输入需要备份的文件名称...')
    Old_File = 'thesis1121.txt'
    if not Old_File:
        print('找不到您要备份的文件，请重新输入...')
        pass
    else:
        File_list = Old_File.split('.')
        pass

    if len(File_list) < 2: #文件名长度不到2，说明没有.文件类型这一部分
        New_File = File_list[0] + '_copy'
        pass
    else:
        New_File = File_list[0] + '_备份.' + File_list[1]
    
    try:
        with open(Old_File,'r',encoding = "utf-8") as Old_f, open(New_File,'w') as New_f:
            while True:
                content = Old_f.read(1024) #一次最多读取1024个字符，防止一次读取太多占内存，循环读取直至读完整个文件
                New_f.write(content)
                if len(content) < 1024:  #当这一次读取的长度不足1024，说明已经读到最后位置了，可以break跳出来了
                    # print(len(content))
                    break
                pass
    except Exception as err:
        print(err)
        pass

CopyFile()







































































