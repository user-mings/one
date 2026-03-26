#type() ---> 获取指定的字面量或变量的数据类型
from types import NoneType

print("Hello Python")

print(type("Hello"))#str
print(type(30))#int
print(type(3.14))#float
print(type(True))#bool
print(type(False))#bool
print(type(None))#NoneType

num = 50
print(type(num))#int

#isinstance(数据,类型) ----> bool值 ----> 判定数据是否是指定的类型, 是:True , 否:False
print(isinstance(num,int))#True
print(isinstance(num,bool))#False
print(isinstance(num,str))#False
print(isinstance(num,float))#False
print(isinstance(num,NoneType))#False
