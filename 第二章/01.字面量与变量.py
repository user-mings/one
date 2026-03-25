#字面量的写法
# print(44)#整形(int)
# print(3.24)#浮点型(float)
# print(True)#布尔(bool)
# print(False)#布尔(bool)
# print(None)#空值(NoneType)
# print("Hello Python")#字符串(str)
# print("__________")#字符串(str)
#
# #布尔类型本质是整数类型(Ture - 1,False - 0)
# print(True+1)#2
# print(False-1)#-1

#Ctrl+/ 是注释快捷键

#变量 ----> Python是动态类型语言,一个变量可以不同的字面量(最好用不同的变量)
# num = 3333.4
# print(num)
#
# num = num + 2
# print(num)
#
# num = "OK"
# print(num)
#
# num = True
# print(num)

#案例
# base,incr =20.3,50
# print("未来第一个月的播放总量:",base+incr)
# print("未来第二个月的播放总量:",base+incr+incr)

#案例
# a = 20
# b = 10
# c = a
# a = b
# b = c
# a, b = b, a
# print(a,b)

#练习
a = 100
b = 200
c = 300
# c,a,b = a,b,c
d = a
a = b
b = c
c = d
print(a,b,c)
