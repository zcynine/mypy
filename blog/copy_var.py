#coding=utf-8

#浅拷贝
a = [1, 2, 3]
b = a

print b

a[0] = 0
print a
print b

#互不干扰的浅拷贝
a = [1, 2, 3]
b = a[::] # 这里就是复制了一份a
print b

a[0] = 0
print a
print b


#深拷贝
import copy

a = [0, [1, 2], 3]

b = copy.deepcopy(a)
print a
print b

a[0] = 1
print a
print b

a[1][0] = 0
print a
print b

b[1][0] = 2

print a
print b
