# Python 命令行参数


# # 命令行参数-sys模块
# import sys
# print('参数个数为：', len(sys.argv), '个参数')
# print('参数列表：', str(sys.argv))
# # 在当前目录中的终端里输入 python index12-3.py 1 2 3
# # 返回的是一个列表：参数列表： ['index12-3.py', '1', '2', '3']
# print('参数列表：', str(sys.argv[1:]))
# # 返回 参数列表： ['1', '2', '3']


#命令行参数-argparse模块
import argparse
parse = argparse.ArgumentParser(prog='my - 我的程序1', usage='options', description='my - 编写自定义命令行的文件', 
                                epilog='my - unkown epilog',)

print(parse.print_help())























