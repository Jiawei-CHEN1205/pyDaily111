# lesson 6 HW
# 求三组连续自然数的和：求出1到10、20到30和35到45的三个和
# 100个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三人吃1个馒头。请问大小和尚各多少人？
# 指定一个列表，列表里含有唯一一个只出现过一次的数字。写程序找出这个“独一无二”的数字

#hw1
def sumRange(m,n):
    #计算指定区间(m,n)的连续数字之和
    #使用内置函数sum()
    rsSum = sum(range(m,n+1))
    return(rsSum)
    pass

print(sumRange(1,10))
print(sumRange(20,30))
print(sumRange(35,45))

#hw2
# big = a # small = 100-a
for PerCount in range(1,34):
    if PerCount*3 + (100-PerCount)*(1/3) == 100:
        person = (PerCount,100-PerCount)
        pass
    pass
print('大和尚有{}人 小和尚有{}人'.format(person[0],person[1]))

#hw3 利用集合的去重作用 在你写set(xxx)强制转换xxx为一个集合的时候，就是相当于去了重复
setPre = [22,33,44,55,66,1234,77,88,33,44,1234,66,22,77,55,55,22,33] #88唯一

# set()强制转换为集合
setAAA = set(setPre)

print(setAAA)
for item in setAAA:
    setPre.remove(item) #利用remove() 函数 把设定的原列表setPre里面的所有元素去掉(一遍) 相当于把88也去掉了
    pass
print(setPre)

# set()强制转换为集合 把上述去掉setAAA之后的setPre去重  
# 因为之前的元素（除了88之外）至少有两遍，所以现在得到的余下的setPre至少有一遍重复的元素，去重得到setBBB的话，就是不含88的所有元素的一遍了
setBBB = set(setPre)
print(setBBB)

# 现在setAAA 和setBBB 只差一个元素了 就是88
only = setAAA - setBBB # 差集
print(only) #{88}

















