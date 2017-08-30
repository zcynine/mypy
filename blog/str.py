#coding=utf-8

#查找
s = "abc"
print s.find("b")

#分割
s = "aa12bb12cc"
print s.split('12')

#大小写转换
s = "abc"
print s.upper()
s = "ABC"
print s.lower()

#截取
s = "1234567"
print s[2:5]

#替换
s = "1,2,3"
print s.replace(",", "#")

#连接
s = ['a', 'b', 'c']
print ",".join(s)

#反转
s = "abc"
print s[::-1]