import time
import datetime 

from Modeltest import * # 安装完毕cjw_module-1.0.tar.gz之后就可以在各种文件里面调用这个模块了，而不必非要建在同一个文件目录下
from Modeltest import printInfo  


print(differ(22,19))
print(printInfo())

#返回 2017-12-08 15:00:18.312624
print(datetime.datetime.now()) 

# 时间戳
print(time.time()) #1638708180.107935
#时间戳直接（1512715165.0285344）转成日期格式 2017-12-08, 这两种方式都可以变成只有日期date的格式
print(datetime.date.today())
print(datetime.date.fromtimestamp(time.time()))

print(datetime.date.weekday(datetime.date.today())) # weekday 返回一周的第几天 感觉在套娃

#当前时间+3天:
print(datetime.datetime.now() + datetime.timedelta(3)) 
#当前时间-3天:
print(datetime.datetime.now() + datetime.timedelta(-3)) 
#当前时间+3小时:
print(datetime.datetime.now() + datetime.timedelta(hours=3)) 
#当前时间+30分:
print(datetime.datetime.now() + datetime.timedelta(minutes=30))
#当前时间+3小时30分:
print(datetime.datetime.now() + datetime.timedelta(hours=3,minutes=30))







































